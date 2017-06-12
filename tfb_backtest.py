# -*- coding: utf-8 -*-
#

import os
import arrow
import pandas as pd
import tfb_sys as tfsys
import tfb_tools as tft


def bt_lnkXDat(g10, kcid):
    g20 = pd.DataFrame(columns=tfsys.gidSgn)
    df9 = pd.DataFrame(columns=tfsys.gxdatSgn)
    for i, row in g10.iterrows():
        gid = row['gid']
        fxdat = tfsys.rxdat + gid + '_oz.dat'
        if os.path.exists(fxdat):
            df = pd.read_csv(fxdat, index_col=False,
                             dtype=str)
            c10 = df[df.cid == kcid]

            if len(c10.index) == 1:
                df9 = df9.append(df)
                g20 = g20.append(row.T, ignore_index=True)
    #
    # fss='tmp/df901.dat'
    # df9.to_csv(fss,index=False)
    #
    return df9, g20

#----------fb.bt.1day.xxx


def bt_1d_ret(xtfb):
    # print('\n@bt_1d_ret')
    ret1d = pd.Series(tfsys.retNil, index=tfsys.retSgn)
    ret1d['xtim'], ret1d['cid'], ret1d['num9'] = xtfb.ktimStr, xtfb.kcid, 0
    #
    df9 = xtfb.poolDay
    xnum = len(df9.index)
    if xnum == 0:
        return ret1d
    #
    nlst, flst = ['kwin', 'kwin_sta'], ['pwin9', 'pdraw9', 'plost9']
    tft.fb_df_type4mlst(df9, nlst, flst)
    #
    for i, row in df9.iterrows():
        kwin, kwin2 = row['kwin'], row['kwin_sta']
        if kwin > -1:
            rsgn = 'num' + str(kwin2)
            ret1d['num9'], ret1d[rsgn] = ret1d['num9'] + 1, ret1d[rsgn] + 1
            #
            if kwin == kwin2:
                dmoney = tft.fb_kwin2pdat(kwin, row)
                rsgn = 'nwin' + str(kwin2)
                ret1d['nwin9'], ret1d[rsgn] = ret1d[
                    'nwin9'] + 1, ret1d[rsgn] + 1
                rsgn = 'ret' + str(kwin2)
                ret1d['ret9'], ret1d[rsgn] = ret1d[
                    'ret9'] + dmoney, ret1d[rsgn] + dmoney
                # print(i,'#1',kwin,dmoney)
    #
    xlst = [9, 3, 1, 0]
    for xd in xlst:
        xss = str(xd)
        dn = ret1d['num' + xss]
        if dn > 0:
            ret1d['kret' + xss] = round(ret1d['ret' + xss] / dn * 100, 2)
            ret1d['knum' + xss] = round(ret1d['nwin' + xss] / dn * 100, 2)

    #
    # print(ret1d);
    return ret1d


def bt_1d_anz_1play(xtfb):
    # print('\nbt_1d_anz_1play')
    bars = xtfb.bars
    gid = bars['gid']
    xtfb.kgid = gid
    df = xtfb.xdat10[xtfb.xdat10.gid == gid]
    xkwin = xtfb.funSta(xtfb, df)
    #---trade
    if xkwin != -9:
        xtfb.poolInx.append(gid)
        #
        g10 = bars
        c10 = df[df.cid == xtfb.kcid]
        #
        g10['kwin_sta'], g10['cid'] = xkwin, xtfb.kcid
        g10['pwin9'], g10['pdraw9'], g10['plost9'] = c10[
            'pwin9'][0], c10['pdraw9'][0], c10['plost9'][0]
        #
        xtfb.poolDay = xtfb.poolDay.append(g10.T, ignore_index=True)
        xtfb.poolTrd = xtfb.poolTrd.append(g10.T, ignore_index=True)
        # print(xtfb.poolDay)


def bt_1d_anz(xtfb):
    # 1#day
    #
    for i, row in xtfb.gid10.iterrows():
        xtfb.bars = row
        #
        bt_1d_anz_1play(xtfb)
    #
    if len(xtfb.poolDay.index) > 0:
        ret01 = bt_1d_ret(xtfb)
        if ret01['num9'] > 0:
            xtfb.poolRet = xtfb.poolRet.append(ret01.T, ignore_index=True)
            # print(xtfb.poolRet)


def bt_1dayMain(xtfb):
    xtfb.poolInx, xtfb.xdat10 = [], None
    xtfb.poolDay = pd.DataFrame(columns=tfsys.poolSgn)
    #
    df = tfsys.gids
    g10 = df[df.tplay == xtfb.ktimStr]
    #------  lnk.xdat
    xdat, xtfb.gid10 = bt_lnkXDat(g10, xtfb.kcid)
    if len(xdat.index) > 0:
        #--dat.pre0
        xlst = ['pwin0', 'pdraw0', 'plost0', 'pwin9', 'pdraw9', 'plost9']
        tft.fb_df_type2float(xdat, xlst)
        tft.fb_df_type_xed(xdat)
        #
        xtfb.xdat10 = xdat
        #
        # 2  data.pre
        xtfb.funPre(xtfb)
        # fss='tmp/df901b.dat'
        # xtfb.xdat10.to_csv(fss,index=False)
        #
        # 3  bt.anz&trade #gid -->pool
        bt_1d_anz(xtfb)
        #

#----------bt--main


def bt_main(xtfb, timStr):
    if timStr == '':
        ktim = xtfb.tim_now
    else:
        ktim = arrow.get(timStr)
    #
    nday = tfsys.xnday_down
    #
    tfsys.gids['kwin_sta'] = -9
    xtfb.poolRet = pd.DataFrame(columns=tfsys.retSgn)
    for tc in range(-3, nday):
        xtim = ktim.shift(days=-tc)
        xtimStr = xtim.format('YYYY-MM-DD')
        print('\n', tc, '#', xtimStr)
        #
        if xtim < xtfb.tim0_gid:
            break
        #
        xtfb.ktimStr = xtimStr
        bt_1dayMain(xtfb)
        #


def bt_main_ret(xtfb, fgMsg=False):
    # 1
    ret9 = pd.Series(tfsys.retNil, index=tfsys.retSgn)
    rlst = tfsys.retSgn[1:]
    for rsgn in rlst:
        ret9[rsgn] = xtfb.poolRet[rsgn].sum()
        # print(rsgn,r10[rsgn].sum())
    # 2
    xlst = [9, 3, 1, 0]
    for xd in xlst:
        xss = str(xd)
        dn = ret9['num' + xss]
        if dn > 0:
            ret9['kret' + xss] = round(ret9['ret' + xss] / dn * 100, 2)
            ret9['knum' + xss] = round(ret9['nwin' + xss] / dn * 100, 2)
    # 3
    nlst = ['num9', 'nwin9', 'num3', 'nwin3', 'num1', 'nwin1', 'num0', 'nwin0']
    float_lst = ['kret9', 'kret3', 'kret1', 'kret0', 'knum9',
                 'knum3', 'knum1', 'knum0', 'ret9', 'ret3', 'ret1', 'ret0']
    tft.fb_df_type4mlst(xtfb.poolRet, nlst, float_lst)
    for xsgn in float_lst:
        print xtfb.poolRet[xsgn]
        xtfb.poolRet[xsgn] = round(xtfb.poolRet[xsgn], 2)
        ret9[xsgn] = round(ret9[xsgn], 2)
    # 4
    #--save.dat
    ret9['xtim'], ret9['cid'] = 'sum', xtfb.kcid
    xtfb.poolRet = xtfb.poolRet.append(ret9, ignore_index=True)
    xtfb.poolTrd.to_csv(xtfb.poolTrdFN)
    xtfb.poolRet.to_csv(xtfb.poolRetFN)

    # 5
    if fgMsg:
        print('\nxtfb.poolTrd,足彩推荐')
        print(xtfb.poolTrd.head())
        print('\nxtfb.poolRet，回报率汇总')
        print(xtfb.poolRet.tail())
