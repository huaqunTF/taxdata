import pandas as pd
from collections import OrderedDict
from tqdm import tqdm
from pathlib import Path


CUR_PATH = Path(__file__).resolve().parent
OUTPUT_PATH = Path(CUR_PATH, "data")


def h_rec(rec):

    record = OrderedDict()

    record["hrecord"] = int(rec[0:1])
    record["h_seq"] = int(rec[1:6])
    record["hhpos"] = int(rec[6:8])
    record["hunits"] = int(rec[8:9])
    record["hefaminc"] = int(rec[9:11])
    record["h_respnm"] = int(rec[11:13])
    record["h_year"] = int(rec[13:17])
    record["h_hhtype"] = int(rec[19:20])
    record["h_numper"] = int(rec[20:22])
    record["hnumfam"] = int(rec[22:24])
    record["h_type"] = int(rec[24:25])
    record["h_month"] = int(rec[25:27])
    record["h_mis"] = int(rec[28:29])
    record["h_hhnum"] = int(rec[29:30])
    record["h_livqrt"] = int(rec[30:32])
    record["h_typebc"] = int(rec[32:34])
    record["h_tenure"] = int(rec[34:35])
    record["h_telhhd"] = int(rec[35:36])
    record["h_telavl"] = int(rec[36:37])
    record["h_telint"] = int(rec[37:38])
    record["gereg"] = int(rec[38:39])
    record["gestcen"] = int(rec[39:41])
    record["gestfips"] = int(rec[41:43])
    record["gtcbsa"] = int(rec[43:48])
    record["gtco"] = int(rec[48:51])
    record["gtcbsast"] = int(rec[51:52])
    record["gtmetsta"] = int(rec[52:53])
    record["gtindvpc"] = int(rec[53:54])
    record["gtcbsasz"] = int(rec[54:55])
    record["gtcsa"] = int(rec[55:58])
    record["hunder15"] = int(rec[59:61])
    record["hh5to18"] = int(rec[67:69])
    record["hhotlun"] = int(rec[69:70])
    record["hhotno"] = int(rec[70:71])
    record["hflunch"] = int(rec[71:72])
    record["hflunno"] = int(rec[72:73])
    record["hpublic"] = int(rec[73:74])
    record["hlorent"] = int(rec[74:75])
    record["hfoodsp"] = int(rec[75:76])
    record["hfoodno"] = int(rec[76:77])
    record["hfoodmo"] = int(rec[78:80])
    record["hengast"] = int(rec[84:85])
    record["hengval"] = int(rec[85:89])
    record["hinc_ws"] = int(rec[89:90])
    record["hwsval"] = int(rec[90:97])
    record["hinc_se"] = int(rec[97:98])
    record["hseval"] = int(rec[98:105])
    record["hinc_fr"] = int(rec[105:106])
    record["hfrval"] = int(rec[106:113])
    record["hinc_uc"] = int(rec[113:114])
    record["hucval"] = int(rec[114:121])
    record["hinc_wc"] = int(rec[121:122])
    record["hwcval"] = int(rec[122:129])
    record["hss_yn"] = int(rec[129:130])
    record["hssval"] = int(rec[130:137])
    record["hssi_yn"] = int(rec[137:138])
    record["hssival"] = int(rec[138:144])
    record["hpaw_yn"] = int(rec[144:145])
    record["hpawval"] = int(rec[145:151])
    record["hvet_yn"] = int(rec[151:152])
    record["hvetval"] = int(rec[152:159])
    record["hsur_yn"] = int(rec[159:160])
    record["hsurval"] = int(rec[160:167])
    record["hdis_yn"] = int(rec[167:168])
    record["hdisval"] = int(rec[168:175])
    record["hret_yn"] = int(rec[175:176])
    record["hretval"] = int(rec[176:183])
    record["hint_yn"] = int(rec[183:184])
    record["hintval"] = int(rec[184:191])
    record["hdiv_yn"] = int(rec[191:192])
    record["hdivval"] = int(rec[192:199])
    record["hrnt_yn"] = int(rec[199:200])
    record["hrntval"] = int(rec[200:207])
    record["hed_yn"] = int(rec[207:208])
    record["hedval"] = int(rec[208:215])
    record["hcsp_yn"] = int(rec[215:216])
    record["hcspval"] = int(rec[216:223])
    record["halm_yn"] = int(rec[223:224])
    record["halmval"] = int(rec[224:231])
    record["hfin_yn"] = int(rec[231:232])
    record["hfinval"] = int(rec[232:239])
    record["hoi_yn"] = int(rec[239:240])
    record["hoival"] = int(rec[240:247])
    record["htotval"] = int(rec[247:255])
    record["hearnval"] = int(rec[255:263])
    record["hothval"] = int(rec[263:271])
    record["hhinc"] = int(rec[271:273])
    record["hmcare"] = int(rec[273:274])
    record["hmcaid"] = int(rec[274:275])
    record["hchamp"] = int(rec[275:276])
    record["hhi_yn"] = int(rec[276:277])
    record["hhstatus"] = int(rec[277:278])
    record["hunder18"] = int(rec[278:280])
    record["htop5pct"] = int(rec[280:281])
    record["hpctcut"] = int(rec[281:283])
    record["hsup_wgt"] = float(rec[286:292] + "." + rec[292:294])
    record["h1tenure"] = int(rec[294:295])
    record["h1livqrt"] = int(rec[296:297])
    record["h1telhhd"] = int(rec[298:299])
    record["h1telavl"] = int(rec[299:300])
    record["h1telint"] = int(rec[300:301])
    record["i_hhotlu"] = int(rec[307:308])
    record["i_hhotno"] = int(rec[308:309])
    record["i_hflunc"] = int(rec[309:310])
    record["i_hflunn"] = int(rec[310:311])
    record["i_hpubli"] = int(rec[311:312])
    record["i_hloren"] = int(rec[312:313])
    record["i_hfoods"] = int(rec[313:314])
    record["i_hfdval"] = int(rec[314:315])
    record["i_hfoodn"] = int(rec[315:316])
    record["i_hfoodm"] = int(rec[316:317])
    record["i_hengas"] = int(rec[317:318])
    record["i_hengva"] = int(rec[318:319])
    record["h_idnum2"] = int(rec[319:324])
    record["prop_tax"] = int(rec[331:336])
    record["housret"] = int(rec[336:341])
    record["hrhtype"] = int(rec[341:343])
    record["h_idnum1"] = int(rec[343:358])
    record["i_hunits"] = int(rec[358:359])
    record["hrpaidcc"] = int(rec[366:367])
    record["hprop_val"] = int(rec[367:375])
    record["thprop_val"] = int(rec[375:376])
    record["i_propval"] = int(rec[376:377])
    record["hrnumwic"] = int(rec[382:384])
    record["hrwicyn"] = int(rec[385:386])
    record["hfdval"] = int(rec[386:391])
    record["tcare_val"] = int(rec[391:392])
    record["care_val"] = int(rec[392:398])
    record["i_careval"] = int(rec[398:399])
    record["hpres_mort"] = int(rec[399:400])

    return record


def f_rec(rec):
    """
    Process family record in CPS
    """

    record = OrderedDict()

    record["frecord"] = int(rec[0:1])
    record["fh_seq"] = int(rec[1:6])
    record["ffpos"] = int(rec[6:8])
    record["fkind"] = int(rec[8:9])
    record["ftype"] = int(rec[9:10])
    record["fpersons"] = int(rec[10:12])
    record["fheadidx"] = int(rec[12:14])
    record["fwifeidx"] = int(rec[14:16])
    record["fhusbidx"] = int(rec[16:18])
    record["fspouidx"] = int(rec[18:20])
    record["flastidx"] = int(rec[20:22])
    record["fmlasidx"] = int(rec[22:24])
    record["fownu6"] = int(rec[24:25])
    record["fownu18"] = int(rec[26:27])
    record["frelu6"] = int(rec[27:28])
    record["frelu18"] = int(rec[28:29])
    record["fpctcut"] = int(rec[29:31])
    record["fpovcut"] = int(rec[31:36])
    record["famlis"] = int(rec[36:37])
    record["povll"] = int(rec[37:39])
    record["frspov"] = int(rec[39:41])
    record["frsppct"] = int(rec[41:46])
    record["finc_ws"] = int(rec[46:47])
    record["fwsval"] = int(rec[47:54])
    record["finc_se"] = int(rec[54:55])
    record["fseval"] = int(rec[55:62])
    record["finc_fr"] = int(rec[62:63])
    record["ffrval"] = int(rec[63:70])
    record["finc_uc"] = int(rec[70:71])
    record["fucval"] = int(rec[71:78])
    record["finc_wc"] = int(rec[78:79])
    record["fwcval"] = int(rec[79:86])
    record["finc_ss"] = int(rec[86:87])
    record["fssval"] = int(rec[87:94])
    record["finc_ssi"] = int(rec[94:95])
    record["fssival"] = int(rec[95:101])
    record["finc_paw"] = int(rec[101:102])
    record["fpawval"] = int(rec[102:108])
    record["finc_vet"] = int(rec[108:109])
    record["fvetval"] = int(rec[109:116])
    record["finc_sur"] = int(rec[116:117])
    record["fsurval"] = int(rec[117:124])
    record["finc_dis"] = int(rec[124:125])
    record["fdisval"] = int(rec[125:132])
    record["finc_ret"] = int(rec[132:133])
    record["fretval"] = int(rec[133:140])
    record["finc_int"] = int(rec[140:141])
    record["fintval"] = int(rec[141:148])
    record["finc_div"] = int(rec[148:149])
    record["fdivval"] = int(rec[149:156])
    record["finc_rnt"] = int(rec[156:157])
    record["frntval"] = int(rec[157:164])
    record["finc_ed"] = int(rec[164:165])
    record["fedval"] = int(rec[165:172])
    record["finc_csp"] = int(rec[172:173])
    record["fcspval"] = int(rec[173:180])
    record["finc_alm"] = int(rec[180:181])
    record["falmval"] = int(rec[181:188])
    record["finc_fin"] = int(rec[188:189])
    record["ffinval"] = int(rec[189:196])
    record["finc_oi"] = int(rec[196:197])
    record["foival"] = int(rec[197:204])
    record["ftotval"] = int(rec[204:212])
    record["fearnval"] = int(rec[212:220])
    record["fothval"] = int(rec[220:228])
    record["ftot_r"] = int(rec[228:230])
    record["fspanish"] = int(rec[230:231])
    record["fsup_wgt"] = float(rec[232:238] + "." + rec[238:240])
    record["ffposold"] = int(rec[240:242])
    record["f_mv_fs"] = int(rec[242:246])
    record["f_mv_sl"] = int(rec[246:250])
    record["ffngcare"] = int(rec[250:255])
    record["ffngcaid"] = int(rec[255:260])
    record["fhoussub"] = int(rec[260:263])
    record["ffoodreq"] = int(rec[263:267])
    record["fhousreq"] = int(rec[267:271])
    record["fhip_val"] = int(rec[271:278])
    record["fmoop"] = int(rec[278:285])
    record["fotc_val"] = int(rec[285:291])
    record["fmed_val"] = int(rec[291:298])
    record["i_fhipval"] = int(rec[298:299])

    return record


def p_rec(rec):
    """
    Process person record in CPS
    """
    record = OrderedDict()

    record["precord"] = int(rec[0:1])
    record["ph_seq"] = int(rec[1:6])
    record["pppos"] = int(rec[6:8])
    record["ppposold"] = int(rec[8:10])
    record["a_lineno"] = int(rec[10:12])
    record["a_parent"] = int(rec[12:14])
    record["a_exprrp"] = int(rec[14:16])
    record["perrp"] = int(rec[16:18])
    record["a_age"] = int(rec[18:20])
    record["a_maritl"] = int(rec[20:21])
    record["a_spouse"] = int(rec[21:23])
    record["a_sex"] = int(rec[23:24])
    record["a_hga"] = int(rec[24:26])
    record["prdtrace"] = int(rec[26:28])
    record["p_stat"] = int(rec[28:29])
    record["prpertyp"] = int(rec[29:30])
    record["pehspnon"] = int(rec[30:31])
    record["prdthsp"] = int(rec[31:32])
    record["a_famnum"] = int(rec[32:34])
    record["a_famtyp"] = int(rec[34:35])
    record["a_famrel"] = int(rec[35:36])
    record["a_pfrel"] = int(rec[36:37])
    record["hhdrel"] = int(rec[37:38])
    record["famrel"] = int(rec[38:40])
    record["hhdfmx"] = int(rec[40:42])
    record["parent"] = int(rec[42:43])
    record["age1"] = int(rec[43:45])
    record["phf_seq"] = int(rec[45:47])
    record["pf_seq"] = int(rec[47:49])
    record["pecohab"] = int(rec[49:51])
    record["pelnmom"] = int(rec[51:53])
    record["pelndad"] = int(rec[53:55])
    record["pemomtyp"] = int(rec[55:57])
    record["pedadtyp"] = int(rec[57:59])
    record["peafever"] = int(rec[59:61])
    record["peafwhn1"] = int(rec[61:63])
    record["peafwhn2"] = int(rec[63:65])
    record["peafwhn3"] = int(rec[65:67])
    record["peafwhn4"] = int(rec[67:69])
    record["pedisear"] = int(rec[69:71])
    record["pediseye"] = int(rec[71:73])
    record["pedisrem"] = int(rec[73:75])
    record["pedisphy"] = int(rec[75:77])
    record["pedisdrs"] = int(rec[77:79])
    record["pedisout"] = int(rec[79:81])
    record["prdisflg"] = int(rec[81:83])
    record["penatvty"] = int(rec[83:86])
    record["pemntvty"] = int(rec[86:89])
    record["pefntvty"] = int(rec[89:92])
    record["peinusyr"] = int(rec[92:94])
    record["prcitshp"] = int(rec[94:95])
    record["peridnum"] = int(rec[95:117])
    record["fl_665"] = int(rec[117:118])
    record["prdasian"] = int(rec[118:120])
    record["a_fnlwgt"] = float(rec[138:144] + "." + rec[144:146])
    record["a_ernlwt"] = float(rec[146:152] + "." + rec[152:154])
    record["marsupwt"] = float(rec[154:160] + "." + rec[160:162])
    record["a_hrs1"] = int(rec[162:164])
    record["a_uslft"] = int(rec[164:165])
    record["a_whyabs"] = int(rec[165:166])
    record["a_payabs"] = int(rec[166:167])
    record["peioind"] = int(rec[167:171])
    record["peioocc"] = int(rec[171:175])
    record["a_clswkr"] = int(rec[175:176])
    record["a_wkslk"] = int(rec[176:179])
    record["a_whenlj"] = int(rec[179:180])
    record["a_nlflj"] = int(rec[180:181])
    record["a_wantjb"] = int(rec[181:182])
    record["prerelg"] = int(rec[182:183])
    record["a_uslhrs"] = int(rec[183:185])
    record["a_hrlywk"] = int(rec[185:186])
    record["a_hrspay"] = float(rec[186:188] + "." + rec[188:190])
    record["a_grswk"] = int(rec[190:194])
    record["a_unmem"] = int(rec[194:195])
    record["a_uncov"] = int(rec[195:196])
    record["a_enrlw"] = int(rec[196:197])
    record["a_hscol"] = int(rec[197:198])
    record["a_ftpt"] = int(rec[198:199])
    record["a_lfsr"] = int(rec[199:200])
    record["a_untype"] = int(rec[200:201])
    record["a_wkstat"] = int(rec[201:202])
    record["a_explf"] = int(rec[202:203])
    record["a_wksch"] = int(rec[203:204])
    record["a_civlf"] = int(rec[204:205])
    record["a_ftlf"] = int(rec[205:206])
    record["a_mjind"] = int(rec[206:208])
    record["a_dtind"] = int(rec[208:210])
    record["a_mjocc"] = int(rec[210:212])
    record["a_dtocc"] = int(rec[212:214])
    record["peio1cow"] = int(rec[214:216])
    record["prcow1"] = int(rec[216:217])
    record["pemlr"] = int(rec[217:218])
    record["pruntype"] = int(rec[218:219])
    record["prwkstat"] = int(rec[219:221])
    record["prptrea"] = int(rec[221:223])
    record["prdisc"] = int(rec[223:224])
    record["peabsrsn"] = int(rec[224:226])
    record["prnlfsch"] = int(rec[226:227])
    record["pehruslt"] = int(rec[227:230])
    record["workyn"] = int(rec[250:251])
    record["wrk_ck"] = int(rec[251:252])
    record["wtemp"] = int(rec[252:253])
    record["nwlook"] = int(rec[253:254])
    record["nwlkwk"] = int(rec[254:256])
    record["rsnnotw"] = int(rec[256:257])
    record["wkswork"] = int(rec[257:259])
    record["wkcheck"] = int(rec[259:260])
    record["losewks"] = int(rec[260:261])
    record["lknone"] = int(rec[261:262])
    record["lkweeks"] = int(rec[262:264])
    record["lkstrch"] = int(rec[264:265])
    record["pyrsn"] = int(rec[265:266])
    record["phmemprs"] = int(rec[266:267])
    record["hrswk"] = int(rec[267:269])
    record["hrcheck"] = int(rec[269:270])
    record["ptyn"] = int(rec[270:271])
    record["ptweeks"] = int(rec[271:273])
    record["ptrsn"] = int(rec[273:274])
    record["wexp"] = int(rec[274:276])
    record["wewkrs"] = int(rec[276:277])
    record["welknw"] = int(rec[277:278])
    record["weuemp"] = int(rec[278:279])
    record["earner"] = int(rec[279:280])
    record["clwk"] = int(rec[280:281])
    record["weclw"] = int(rec[281:282])
    record["poccu2"] = int(rec[282:284])
    record["wemocg"] = int(rec[284:286])
    record["weind"] = int(rec[286:288])
    record["wemind"] = int(rec[288:290])
    record["ljcw"] = int(rec[290:291])
    record["industry"] = int(rec[291:295])
    record["occup"] = int(rec[295:299])
    record["noemp"] = int(rec[299:300])
    record["nxtres"] = int(rec[320:322])
    record["mig_cbst"] = int(rec[322:323])
    record["migsame"] = int(rec[323:324])
    record["mig_reg"] = int(rec[324:325])
    record["mig_st"] = int(rec[325:327])
    record["mig_dscp"] = int(rec[327:328])
    record["gediv"] = int(rec[328:329])
    record["mig_div"] = int(rec[329:331])
    record["mig_mtr1"] = int(rec[331:333])
    record["mig_mtr3"] = int(rec[333:334])
    record["mig_mtr4"] = int(rec[334:335])
    record["ern_yn"] = int(rec[351:352])
    record["ern_srce"] = int(rec[352:353])
    record["ern_otr"] = int(rec[353:354])
    record["ern_val"] = int(rec[354:361])
    record["wageotr"] = int(rec[361:362])
    record["wsal_yn"] = int(rec[362:363])
    record["wsal_val"] = int(rec[363:370])
    record["ws_val"] = int(rec[370:377])
    record["seotr"] = int(rec[377:378])
    record["semp_yn"] = int(rec[378:379])
    record["semp_val"] = int(rec[379:386])
    record["se_val"] = int(rec[386:392])
    record["frmotr"] = int(rec[392:393])
    record["frse_yn"] = int(rec[393:394])
    record["frse_val"] = int(rec[394:401])
    record["frm_val"] = int(rec[401:407])
    record["uc_yn"] = int(rec[407:408])
    record["subuc"] = int(rec[408:409])
    record["strkuc"] = int(rec[409:410])
    record["uc_val"] = int(rec[410:415])
    record["wc_yn"] = int(rec[415:416])
    record["wc_type"] = int(rec[416:417])
    record["wc_val"] = int(rec[417:422])
    record["ss_yn"] = int(rec[422:423])
    record["ss_val"] = int(rec[423:428])
    record["resnss1"] = int(rec[428:429])
    record["resnss2"] = int(rec[429:430])
    record["sskidyn"] = int(rec[430:431])
    record["ssi_yn"] = int(rec[431:432])
    record["ssi_val"] = int(rec[432:437])
    record["resnssi1"] = int(rec[437:438])
    record["resnssi2"] = int(rec[438:439])
    record["ssikidyn"] = int(rec[439:440])
    record["paw_yn"] = int(rec[440:441])
    record["paw_typ"] = int(rec[441:442])
    record["paw_mon"] = int(rec[442:444])
    record["paw_val"] = int(rec[444:449])
    record["vet_yn"] = int(rec[449:450])
    record["vet_typ1"] = int(rec[450:451])
    record["vet_typ2"] = int(rec[451:452])
    record["vet_typ3"] = int(rec[452:453])
    record["vet_typ4"] = int(rec[453:454])
    record["vet_typ5"] = int(rec[454:455])
    record["vet_qva"] = int(rec[455:456])
    record["vet_val"] = int(rec[456:461])
    record["sur_yn"] = int(rec[461:462])
    record["sur_sc1"] = int(rec[462:464])
    record["sur_sc2"] = int(rec[464:466])
    record["sur_val1"] = int(rec[466:471])
    record["sur_val2"] = int(rec[471:476])
    record["srvs_val"] = int(rec[476:482])
    record["dis_hp"] = int(rec[482:483])
    record["dis_cs"] = int(rec[483:484])
    record["dis_yn"] = int(rec[484:485])
    record["dis_sc1"] = int(rec[485:487])
    record["dis_sc2"] = int(rec[487:489])
    record["dis_val1"] = int(rec[489:494])
    record["dis_val2"] = int(rec[494:499])
    record["dsab_val"] = int(rec[499:505])
    record["ret_yn"] = int(rec[505:506])
    record["ret_sc1"] = int(rec[506:507])
    record["ret_sc2"] = int(rec[507:508])
    record["ret_val1"] = int(rec[508:513])
    record["ret_val2"] = int(rec[513:518])
    record["rtm_val"] = int(rec[518:524])
    record["int_yn"] = int(rec[524:525])
    record["int_val"] = int(rec[525:530])
    record["div_yn"] = int(rec[530:531])
    record["div_non"] = int(rec[531:532])
    record["div_val"] = int(rec[532:538])
    record["rnt_yn"] = int(rec[538:539])
    record["rnt_val"] = int(rec[539:544])
    record["ed_yn"] = int(rec[544:545])
    record["oed_typ1"] = int(rec[545:546])
    record["oed_typ2"] = int(rec[546:547])
    record["oed_typ3"] = int(rec[547:548])
    record["ed_val"] = int(rec[548:553])
    record["csp_yn"] = int(rec[553:554])
    record["csp_val"] = int(rec[554:559])
    record["alm_yn"] = int(rec[559:560])
    record["alm_val"] = int(rec[560:565])
    record["fin_yn"] = int(rec[565:566])
    record["fin_val"] = int(rec[566:571])
    record["oi_off"] = int(rec[571:573])
    record["oi_yn"] = int(rec[573:574])
    record["oi_val"] = int(rec[574:579])
    record["ptotval"] = int(rec[579:587])
    record["pearnval"] = int(rec[587:595])
    record["pothval"] = int(rec[595:603])
    record["ptot_r"] = int(rec[603:605])
    record["perlis"] = int(rec[605:606])
    record["pov_univ"] = int(rec[606:607])
    record["wicyn"] = int(rec[607:608])
    record["mcare"] = int(rec[628:629])
    record["p_mvcare"] = int(rec[629:634])
    record["mcaid"] = int(rec[634:635])
    record["p_mvcaid"] = int(rec[635:640])
    record["champ"] = int(rec[640:641])
    record["hi_yn"] = int(rec[641:642])
    record["hiown"] = int(rec[642:643])
    record["hiemp"] = int(rec[643:644])
    record["hipaid"] = int(rec[644:645])
    record["emcontrb"] = int(rec[645:649])
    record["hi"] = int(rec[649:650])
    record["hityp"] = int(rec[650:651])
    record["dephi"] = int(rec[651:652])
    record["hilin1"] = int(rec[652:654])
    record["hilin2"] = int(rec[654:656])
    record["paid"] = int(rec[656:657])
    record["hiout"] = int(rec[657:658])
    record["priv"] = int(rec[658:659])
    record["prityp"] = int(rec[659:660])
    record["depriv"] = int(rec[660:661])
    record["pilin1"] = int(rec[661:663])
    record["pilin2"] = int(rec[663:665])
    record["pout"] = int(rec[665:666])
    record["out"] = int(rec[666:667])
    record["care"] = int(rec[667:668])
    record["caid"] = int(rec[668:669])
    record["mon"] = int(rec[669:671])
    record["oth"] = int(rec[671:672])
    record["otyp_1"] = int(rec[672:673])
    record["otyp_2"] = int(rec[673:674])
    record["otyp_3"] = int(rec[674:675])
    record["otyp_4"] = int(rec[675:676])
    record["otyp_5"] = int(rec[676:677])
    record["othstper"] = int(rec[677:678])
    record["othstyp1"] = int(rec[678:680])
    record["othstyp2"] = int(rec[680:682])
    record["othstyp3"] = int(rec[682:684])
    record["othstyp4"] = int(rec[684:686])
    record["othstyp5"] = int(rec[686:688])
    record["othstyp6"] = int(rec[688:690])
    record["hea"] = int(rec[690:691])
    record["ihsflg"] = int(rec[691:692])
    record["ahiper"] = int(rec[692:693])
    record["ahityp1"] = int(rec[693:695])
    record["ahityp2"] = int(rec[695:697])
    record["ahityp3"] = int(rec[697:699])
    record["ahityp4"] = int(rec[699:701])
    record["ahityp5"] = int(rec[701:703])
    record["ahityp6"] = int(rec[703:705])
    record["pchip"] = int(rec[705:706])
    record["cov_gh"] = int(rec[706:707])
    record["cov_hi"] = int(rec[707:708])
    record["ch_mc"] = int(rec[708:709])
    record["ch_hi"] = int(rec[709:710])
    record["marg_tax"] = int(rec[723:725])
    record["ctc_crd"] = int(rec[725:730])
    record["penplan"] = int(rec[730:731])
    record["penincl"] = int(rec[731:732])
    record["filestat"] = int(rec[732:733])
    record["dep_stat"] = int(rec[733:735])
    record["eit_cred"] = int(rec[735:739])
    record["actc_crd"] = int(rec[739:743])
    record["fica"] = int(rec[743:748])
    record["fed_ret"] = int(rec[748:754])
    record["agi"] = int(rec[754:761])
    record["tax_inc"] = int(rec[764:771])
    record["fedtax_bc"] = int(rec[771:777])
    record["fedtax_ac"] = int(rec[777:783])
    record["statetax_bc"] = int(rec[783:789])
    record["statetax_ac"] = int(rec[789:795])
    record["prswkxpns"] = int(rec[795:799])
    record["paidccyn"] = int(rec[799:800])
    record["paidcyna"] = int(rec[800:801])
    record["moop"] = int(rec[801:808])
    record["phip_val"] = int(rec[808:814])
    record["potc_val"] = int(rec[814:819])
    record["pmed_val"] = int(rec[819:825])
    record["chsp_val"] = int(rec[825:830])
    record["chsp_yn"] = int(rec[830:831])
    record["chelsew_yn"] = int(rec[831:832])
    record["axrrp"] = int(rec[852:853])
    record["axage"] = int(rec[853:854])
    record["axmaritl"] = int(rec[854:855])
    record["axspouse"] = int(rec[855:856])
    record["axsex"] = int(rec[856:857])
    record["axhga"] = int(rec[857:858])
    record["pxrace1"] = int(rec[858:860])
    record["pxhspnon"] = int(rec[860:862])
    record["pxcohab"] = int(rec[862:864])
    record["pxlnmom"] = int(rec[864:866])
    record["pxlndad"] = int(rec[866:868])
    record["pxmomtyp"] = int(rec[868:870])
    record["pxdadtyp"] = int(rec[870:872])
    record["pxafever"] = int(rec[872:874])
    record["pxafwhn1"] = int(rec[874:876])
    record["pxdisear"] = int(rec[876:878])
    record["pxdiseye"] = int(rec[878:880])
    record["pxdisrem"] = int(rec[880:882])
    record["pxdisphy"] = int(rec[882:884])
    record["pxdisdrs"] = int(rec[884:886])
    record["pxdisout"] = int(rec[886:888])
    record["pxnatvty"] = int(rec[888:890])
    record["pxmntvty"] = int(rec[890:892])
    record["pxfntvty"] = int(rec[892:894])
    record["pxinusyr"] = int(rec[894:896])
    record["prwernal"] = int(rec[896:897])
    record["prhernal"] = int(rec[897:898])
    record["axhrs"] = int(rec[898:899])
    record["axwhyabs"] = int(rec[899:900])
    record["axpayabs"] = int(rec[900:901])
    record["axclswkr"] = int(rec[901:902])
    record["axnlflj"] = int(rec[902:903])
    record["axuslhrs"] = int(rec[903:904])
    record["axhrlywk"] = int(rec[904:905])
    record["axunmem"] = int(rec[905:906])
    record["axuncov"] = int(rec[906:907])
    record["axenrlw"] = int(rec[907:908])
    record["axhscol"] = int(rec[908:909])
    record["axftpt"] = int(rec[909:910])
    record["axlfsr"] = int(rec[910:911])
    record["i_workyn"] = int(rec[911:912])
    record["i_wtemp"] = int(rec[912:913])
    record["i_nwlook"] = int(rec[913:914])
    record["i_nwlkwk"] = int(rec[914:915])
    record["i_rsnnot"] = int(rec[915:916])
    record["i_wkswk"] = int(rec[916:917])
    record["i_wkchk"] = int(rec[917:918])
    record["i_losewk"] = int(rec[918:919])
    record["i_lkweek"] = int(rec[919:920])
    record["i_lkstr"] = int(rec[920:921])
    record["i_pyrsn"] = int(rec[921:922])
    record["i_phmemp"] = int(rec[922:923])
    record["i_hrswk"] = int(rec[923:924])
    record["i_hrchk"] = int(rec[924:925])
    record["i_ptyn"] = int(rec[925:926])
    record["i_ptwks"] = int(rec[926:927])
    record["i_ptrsn"] = int(rec[927:928])
    record["i_ljcw"] = int(rec[928:929])
    record["i_indus"] = int(rec[929:930])
    record["i_occup"] = int(rec[930:931])
    record["i_noemp"] = int(rec[931:932])
    record["i_nxtres"] = int(rec[932:933])
    record["i_mig1"] = int(rec[933:934])
    record["i_mig2"] = int(rec[934:936])
    record["i_mig3"] = int(rec[936:937])
    record["i_disyn"] = int(rec[937:938])
    record["i_ernyn"] = int(rec[938:939])
    record["i_ernsrc"] = int(rec[939:940])
    record["i_ernval"] = int(rec[940:941])
    record["i_retsc2"] = int(rec[941:942])
    record["i_wsyn"] = int(rec[942:943])
    record["i_wsval"] = int(rec[943:944])
    record["i_seyn"] = int(rec[944:945])
    record["i_seval"] = int(rec[945:946])
    record["i_frmyn"] = int(rec[946:947])
    record["i_frmval"] = int(rec[947:948])
    record["i_ucyn"] = int(rec[948:949])
    record["i_ucval"] = int(rec[949:950])
    record["i_wcyn"] = int(rec[950:951])
    record["i_wctyp"] = int(rec[951:952])
    record["i_wcval"] = int(rec[952:953])
    record["i_ssyn"] = int(rec[953:954])
    record["i_ssval"] = int(rec[954:955])
    record["resnssa"] = int(rec[955:956])
    record["i_ssiyn"] = int(rec[956:957])
    record["sskidyna"] = int(rec[957:958])
    record["i_ssival"] = int(rec[958:959])
    record["resnssia"] = int(rec[959:960])
    record["i_pawyn"] = int(rec[960:961])
    record["ssikdyna"] = int(rec[961:962])
    record["i_pawtyp"] = int(rec[962:963])
    record["i_pawmo"] = int(rec[963:964])
    record["i_pawval"] = int(rec[964:965])
    record["i_vetyn"] = int(rec[965:966])
    record["i_vettyp"] = int(rec[966:967])
    record["i_vetqva"] = int(rec[967:968])
    record["i_vetval"] = int(rec[968:969])
    record["i_suryn"] = int(rec[969:970])
    record["i_sursc1"] = int(rec[970:971])
    record["i_sursc2"] = int(rec[971:972])
    record["i_survl1"] = int(rec[972:973])
    record["i_survl2"] = int(rec[973:974])
    record["i_dishp"] = int(rec[974:975])
    record["i_discs"] = int(rec[975:976])
    record["i_dissc1"] = int(rec[976:977])
    record["i_dissc2"] = int(rec[977:978])
    record["i_disvl1"] = int(rec[978:979])
    record["i_disvl2"] = int(rec[979:980])
    record["i_retyn"] = int(rec[980:981])
    record["i_retsc1"] = int(rec[981:982])
    record["i_retvl1"] = int(rec[982:983])
    record["i_retvl2"] = int(rec[983:984])
    record["i_intyn"] = int(rec[984:985])
    record["i_intval"] = int(rec[985:986])
    record["i_divyn"] = int(rec[986:987])
    record["i_divval"] = int(rec[987:988])
    record["i_rntyn"] = int(rec[988:989])
    record["i_rntval"] = int(rec[989:990])
    record["i_edyn"] = int(rec[990:991])
    record["i_edtyp1"] = int(rec[991:992])
    record["i_edtyp2"] = int(rec[992:993])
    record["i_oedval"] = int(rec[993:994])
    record["i_cspyn"] = int(rec[994:995])
    record["i_cspval"] = int(rec[995:996])
    record["i_almyn"] = int(rec[996:997])
    record["i_almval"] = int(rec[997:998])
    record["i_finyn"] = int(rec[998:999])
    record["i_finval"] = int(rec[999:1000])
    record["i_oival"] = int(rec[1000:1001])
    record["wicyna"] = int(rec[1001:1002])
    record["i_hi"] = int(rec[1002:1003])
    record["i_dephi"] = int(rec[1003:1004])
    record["i_paid"] = int(rec[1004:1005])
    record["i_hiout"] = int(rec[1005:1006])
    record["i_priv"] = int(rec[1006:1007])
    record["i_depriv"] = int(rec[1007:1008])
    record["i_pout"] = int(rec[1008:1009])
    record["i_out"] = int(rec[1009:1010])
    record["i_care"] = int(rec[1010:1011])
    record["i_caid"] = int(rec[1011:1012])
    record["i_mon"] = int(rec[1012:1013])
    record["i_oth"] = int(rec[1013:1014])
    record["i_otyp"] = int(rec[1014:1015])
    record["i_ostper"] = int(rec[1015:1016])
    record["i_ostyp"] = int(rec[1016:1017])
    record["i_hea"] = int(rec[1017:1018])
    record["iahiper"] = int(rec[1018:1019])
    record["iahityp"] = int(rec[1019:1020])
    record["i_pchip"] = int(rec[1020:1021])
    record["i_penpla"] = int(rec[1021:1022])
    record["i_peninc"] = int(rec[1022:1023])
    record["i_phipval"] = int(rec[1023:1024])
    record["i_potcval"] = int(rec[1024:1025])
    record["i_pmedval"] = int(rec[1025:1026])
    record["i_chspval"] = int(rec[1026:1027])
    record["i_chspyn"] = int(rec[1027:1028])
    record["i_chelsewyn"] = int(rec[1028:1029])
    record["a_werntf"] = int(rec[1049:1050])
    record["a_herntf"] = int(rec[1050:1051])
    record["tcernval"] = int(rec[1051:1052])
    record["tcwsval"] = int(rec[1052:1053])
    record["tcseval"] = int(rec[1053:1054])
    record["tcffmval"] = int(rec[1054:1055])
    record["tsurval1"] = int(rec[1055:1056])
    record["tsurval2"] = int(rec[1056:1057])
    record["tdisval1"] = int(rec[1057:1058])
    record["tdisval2"] = int(rec[1058:1059])
    record["tretval1"] = int(rec[1059:1060])
    record["tretval2"] = int(rec[1060:1061])
    record["tint_val"] = int(rec[1061:1062])
    record["tdiv_val"] = int(rec[1062:1063])
    record["trnt_val"] = int(rec[1063:1064])
    record["ted_val"] = int(rec[1064:1065])
    record["tcsp_val"] = int(rec[1065:1066])
    record["talm_val"] = int(rec[1066:1067])
    record["tfin_val"] = int(rec[1067:1068])
    record["toi_val"] = int(rec[1068:1069])
    record["tphip_val"] = int(rec[1069:1070])
    record["tpotc_val"] = int(rec[1070:1071])
    record["tpmed_val"] = int(rec[1071:1072])
    record["tchsp_val"] = int(rec[1072:1073])

    return record


def create_cps(dat_file, year, export=True):
    """
    Convert a .DAT copy of the CPS to a CSV
    """

    # read in file
    print("Reading DAT file")
    with Path(dat_file).open("r") as f:
        cps = [line.strip() for line in f.readlines()]

    # list to hold the records
    cps_list = []
    print("Creating Records")
    for record in tqdm(cps):
        rec_type = record[0]
        # household records
        if rec_type == "1":
            household = h_rec(record)
        # family record
        elif rec_type == "2":
            family = f_rec(record)
        # person record
        elif rec_type == "3":
            person = p_rec(record)
            full_rec = {**household, **family, **person}
            cps_list.append(full_rec)

    print("Converting to DataFrame")
    cpsmar = pd.DataFrame(cps_list).fillna(0)
    if export:
        print("Exporting")
        export_path = Path(OUTPUT_PATH, f"cpsmar{year}.csv")
        cpsmar.to_csv(export_path, index=False)

    return cpsmar


if __name__ == "__main__":
    create_cps(Path(CUR_PATH, "data", "asec2014_pubuse_tax_fix_5x8_2017.dat"), 2014)
