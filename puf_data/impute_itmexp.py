"""
Script that imputes itemized expense amounts to non-itemizers in puf.csv file.
"""
import numpy as np
import pandas as pd
import statsmodels.api as sm


dump0 = True
dump1 = True
calibrating = True


def impute(ievar, logit_prob_af, log_amount_af,
           logit_x_vars, ols_x_vars,
           itemizer_data, nonitemizer_data):
    """
    Function that estimates imputation equations for ievar with itemizer_data
    using the lists of exogenous variables in logit_x_vars and ols_x_vars.
    The estimated equations are then used to impute amounts for ievar for
    nonitemizers with the imputed nonitemizer amounts being returned.
    """
    if dump1:
        print '*** IMPUTE({}):'.format(ievar)
    # estimate Logit parameters for probability of having a positive amount
    logit_y = (itemizer_data[ievar] > 0).astype(int)
    logit_x = itemizer_data[logit_x_vars]
    logit_res = sm.Logit(logit_y, logit_x).fit(disp=0)
    x_b = logit_res.predict(nonitemizer_data[logit_x_vars], linear=True)
    exp_x_b = np.exp(x_b + logit_prob_af[ievar])
    adj_prob = exp_x_b / (1.0 + exp_x_b)
    np.random.seed(int(ievar[1:]))
    urn = np.random.uniform(size=len(x_b))
    positive_imputed = np.where(urn < adj_prob, True, False)
    if dump1:
        print logit_res.summary()
        print adj_prob.head()
        print positive_imputed.mean()
        print len(nonitemizer_data)
    # estimate OLS parameters for the positive amount using a sample of
    # itemizers who have positive ievar amounts than are less than the
    # itemizer's standard deduction amount
    # (1) This sample limitation is one part of an ad hoc procedure to deal
    # with the Heckman sample selection problems present in this imputation
    # process.
    tpi_data = itemizer_data[(itemizer_data[ievar] > 0) &
                             (itemizer_data[ievar] < itemizer_data['stdded'])]
    ols_y = np.log(tpi_data[ievar])
    ols_x = tpi_data[ols_x_vars]
    ols_res = sm.OLS(ols_y, ols_x).fit()
    ols_se = np.sqrt(ols_res.scale)
    error = np.random.normal(loc=0.0, scale=ols_se,
                             size=len(nonitemizer_data))
    raw_imputed_amt = ols_res.predict(nonitemizer_data[ols_x_vars]) + error
    # (2) Limiting the imputed amount to be no more than the standard
    # deduction is a second part of the ad hoc procedure to deal with the
    # Heckman sample selection problems present in this imputation process.
    log_stdded = np.log(nonitemizer_data['stdded'])
    cap_imputed_amt = np.where(raw_imputed_amt > log_stdded,
                               log_stdded, raw_imputed_amt)
    adj_imputed_amt = cap_imputed_amt + log_amount_af[ievar]
    imputed_amount = np.where(positive_imputed,
                              np.exp(adj_imputed_amt).round().astype(int), 0)
    if dump1:
        print 'size of {} OLS sample = {}'.format(ievar, len(ols_y))
        print 'max {} value = {}'.format(ievar, ols_y.max())
        print 'avg {} value = {:.2f}'.format(ievar, ols_y.mean())
        print ols_res.summary()
        print 'OLS std error of regression = {:.2f}'.format(ols_se)
        print 'mean cap_imputed_amt = {:.3f}'.format(cap_imputed_amt.mean())
        print 'mean adj_imputed_amt = {:.3f}'.format(adj_imputed_amt.mean())
        print 'mean imputed_amount = {:.2f}'.format(imputed_amount.mean())
    # return imputed_amount array
    return imputed_amount


def check(iev, nonitemizer_data, target_cnt, target_amt):
    """
    Function that returns error message if weighted nonitemizer_data for iev
    does not imply filing unit counts and itemized expenses amounts that are
    close to the targets.
    """
    max_diff = 0.2
    var = nonitemizer_data[iev]
    pos = var > 0
    wgt = nonitemizer_data['s006'] * 0.01
    assert len(var) == len(wgt)
    wcnt = wgt[pos].sum() * 1e-6  # millions of filing units
    wamt = (var[pos] * wgt[pos]).sum() * 1e-9  # billions of dollars
    msg = ''
    if not np.allclose([wcnt], [target_cnt[iev]], rtol=0.0, atol=max_diff):
        msg += '\nNONITEMIZER {}>0 CNT TARGET ACTUAL= {:.1f} {:.1f}'.format(
            iev, target_cnt[iev], wcnt
        )
    if not np.allclose([wamt], [target_amt[iev]], rtol=0.0, atol=max_diff):
        msg += '\nNONITEMIZER {}>0 AMT TARGET ACTUAL= {:.1f} {:.1f}'.format(
            iev, target_amt[iev], wamt
        )
    return msg


# read in puf.csv file
alldata = pd.read_csv('puf.csv')

# specify variable names of itemized-expense variables
iev_names = ['e18400',  # state and local taxes
             'e18500',  # real-estate taxes
             'e19200',  # interest paid
             'e19800',  # charity cash contributions
             'e20100',  # charity non-cash contributions
             'e20400',  # misc itemizable expenses
             'e17500',  # medical expenses
             'g20500']  # gross casualty/theft loss

def standard_deduction(row):
    """
    Specifies 2011 standard deduction amount by MARS
    """
    if row['MARS'] == 1 :
        return 5800   # single
    elif row['MARS'] == 2:
        return 11600  # married filing jointly
    elif row['MARS'] == 3:
        return 5800   # married filing separately
    elif row['MARS'] == 4:
        return 8500   # head of household
    else:
        raise ValueError('illegal value of MARS')

# extract selected variables and construct new variables
varnames = iev_names + ['MARS', 'filer', 's006']
data = alldata[varnames].copy()
data['stdded'] = data.apply(standard_deduction, axis=1)
data['sum_itmexp'] = data[iev_names].sum(axis=1)
data['itemizer'] = np.where(data['sum_itmexp'] > data['stdded'], 1, 0)
data['constant'] = 1

# separate all the data into data for itemizers and data for nonitemizers
itemizer_data = data[data['itemizer'] == 1].copy()
nonitemizer_data = data[data['itemizer'] == 0].copy()
    
# descriptive statistics for the data variables
if dump0:
    print 'ALL raw count = {:6d}'.format(len(data))
    print 'PUF raw count = {:6d}'.format(len(data[data['filer'] == 1]))
    print 'CPS raw count = {:6d}'.format(len(data[data['filer'] == 0]))
    print 'PUF fraction of ALL = {:.4f}'.format(data['filer'].mean())
    ier = data['itemizer']
    print 'ALL itemizer mean = {:.4f}'.format(ier.mean())
    print 'PUF itemizer mean = {:.4f}'.format(ier[data['filer'] == 1].mean())
    print 'CPS itemizer mean = {:.4f}'.format(ier[data['filer'] == 0].mean())
    for iev in iev_names:
        var = itemizer_data[iev]
        varpos = var > 0
        print '{} with {}>0 = {:.4f}  {:.2f}'.format(
            'frac and mean for itemizers',
            iev, varpos.mean(), var[varpos].mean()
        )
    for iev in iev_names:
        var = nonitemizer_data[iev]
        varpos = var > 0
        print 'frac of non-itemizers with {}>0 = {:.4f}'.format(iev,
                                                                varpos.mean())

# specify 2011 JCT count/amount targets for nonitemizers
target_cnt = dict(zip(iev_names, [0.0]*len(iev_names)))
target_amt = dict(zip(iev_names, [0.0]*len(iev_names)))
target_cnt['e18400'] = 113.2
target_amt['e18400'] = 128.1
target_cnt['e18500'] = 34.7
target_amt['e18500'] = 46.2
target_cnt['e19200'] = 16.7
target_amt['e19200'] = 58.5
target_cnt['e19800'] = 63.0
target_amt['e19800'] = 27.7
target_cnt['e20100'] = 31.5
target_amt['e20100'] = 15.6
target_cnt['e20400'] = 16.2
target_amt['e20400'] = 18.6 
target_cnt['e17500'] = 5.5
target_amt['e17500'] = 20.4

# specify logit-probability and log-amount additive factors
logit_prob_af = dict(zip(iev_names, [0.0]*len(iev_names)))
log_amount_af = dict(zip(iev_names, [0.0]*len(iev_names)))
logit_prob_af['e18400'] = 1.49
log_amount_af['e18400'] = -1.04
logit_prob_af['e18500'] = -3.07
log_amount_af['e18500'] = -0.98
logit_prob_af['e19200'] = -3.0
log_amount_af['e19200'] = -0.21

logit_prob_af['e19800'] = 0.0
log_amount_af['e19800'] = 0.0
logit_prob_af['e20100'] = 0.0
log_amount_af['e20100'] = 0.0
logit_prob_af['e20400'] = 0.0
log_amount_af['e20400'] = 0.0
logit_prob_af['e17500'] = 0.0
log_amount_af['e17500'] = 0.0

# estimate itemizer equations and use to impute itmexp amounts for nonitemizers
logit_prob_vars = ['constant']
log_amount_vars = ['constant']
errmsg = ''
for iev in iev_names:
    if iev == 'g20500':
        nonitemizer_data['g20500'] = 0
    else:
        nonitemizer_data[iev] = impute(iev, logit_prob_af, log_amount_af,
                                       logit_prob_vars, log_amount_vars,
                                       itemizer_data, nonitemizer_data)
    errmsg += check(iev, nonitemizer_data, target_cnt, target_amt)
    # add imputed variable to exogenous variable lists to better estimate
    # correlation between the imputed variables
    logit_prob_vars.append(iev)
    log_amount_vars.append(iev)
    if calibrating and iev == 'e19200':  # TODO: remove after finished
        break
if errmsg:
    if calibrating:
        print errmsg
    else:
        raise ValueError(errmsg)

# set imputed itmexp variable values in alldata
combined_data = pd.concat([nonitemizer_data, itemizer_data]).sort_index()
for iev in iev_names:
    alldata[iev] = combined_data[iev]

# write augmented puf-new.csv file
alldata.to_csv('puf-new.csv', index=False, float_format='%.2f')


"""
if __name__ == "__main__":
    read in puf.csv
    call main() function
    alldata.to_csv('puf-new.csv', index=False, float_format='%.2f')
"""
