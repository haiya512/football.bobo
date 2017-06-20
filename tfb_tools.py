# -*- coding: utf-8 -*-
'''

'''

import arrow
import pandas as pd
from bs4 import BeautifulSoup
#
from concurrent.futures import ThreadPoolExecutor, as_completed
import zsys
import ztools as zt
import ztools_str as zstr
import ztools_web as zweb
import ztools_data as zdat
#
import tfb_sys as tfsys
import tfb_strategy as tfsty


def fb_df_type_xed(df):
    df['qj'] = df['qj'].astype(int)
    df['qs'] = df['qs'].astype(int)
    df['qr'] = df['qr'].astype(int)
    df['kwin'] = df['kwin'].astype(int)
    df['kwinrq'] = df['kwinrq'].astype(int)


def fb_df_type2float(df, xlst):
    for xsgn in xlst:
        df[xsgn] = df[xsgn].astype(float)


def fb_df_type4mlst(df, nlst, flst):
    for xsgn in nlst:
        df[xsgn] = df[xsgn].astype(int)

    for xsgn in flst:
        df[xsgn] = df[xsgn].astype(float)


def fb_init(rs0='./', fgid=''):
    # 给定义的类赋初始值
    xtfb = tfsys.zTopFoolball()
    xtfb.tim_now = arrow.now()
    xtfb.timStr_now = xtfb.tim_now.format('YYYY-MM-DD')
    xtfb.tim0 = xtfb.tim_now
    xtfb.tim0Str = xtfb.timStr_now
    # print('now:', zt.tim_now_str())

    # xtfb.pools=[]
    xtfb.kcid = '1'  # 官方,3=Bet365
    xtfb.funPre = tfsty.sta00_pre
    xtfb.funSta = tfsty.sta00_sta
    #
    today_date = xtfb.timStr_now
    xtfb.poolTrdFN = 'log/poolTrd_' + today_date + '.csv'
    xtfb.poolRetFN = 'log/poolRet_' + today_date + '.csv'
    # 定义存放数据的目录
    if rs0:
        tfsys.rdat = rs0
        tfsys.rxdat = rs0 + 'xdat/'
        tfsys.rhtmOuzhi = rs0 + 'xhtm/htm_oz/'
        tfsys.rhtmYazhi = rs0 + 'xhtm/htm_az/'
        tfsys.rhtmShuju = rs0 + 'xhtm/htm_sj/'

    # 4
    if fgid:
        tfsys.gidsFN = fgid
        # xtfb.gids=pd.read_csv(fgid,index_col=0,dtype=str,encoding='gbk')
        tfsys.gids = pd.read_csv(fgid, index_col=False, dtype=str)
        fb_df_type_xed(tfsys.gids)
        tfsys.gidsNum = len(tfsys.gids.index)
        xtfb.gid_tim0str = tfsys.gids['tplay'].min()
        xtfb.gid_tim9str = tfsys.gids['tplay'].max()

        tim0 = arrow.get(xtfb.gid_tim0str)
        tim9 = arrow.get(xtfb.gid_tim9str)

        xtfb.gid_nday, = zt.timNDay('', tim0)
        xtfb.gid_nday_tim9 = zt.timNDay('', tim9)

        print('gid tim0: {0}, nday: {1}'.format(
            xtfb.gid_tim0str, xtfb.gid_nday))
        print('gid tim9: {0}, nday: {1}'.format(
            xtfb.gid_tim9str, xtfb.gid_nday_tim9))

    return xtfb


def fb_tweekXed(tstr):
    str_week = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
    str_inx = ['1', '2', '3', '4', '5', '6', '0']
    tstr = zstr.str_mxrep(tstr, str_week, str_inx)
    #
    return tstr


def fb_kwin4qnum(jq, sq, rq=0):
    if (jq < 0) or (sq < 0):
        return -1
    #
    jqk = jq + rq  # or -rq
    if jqk > sq:
        kwin = 3
    elif jqk < sq:
        kwin = 0
    else:
        kwin = 1
    #
    return kwin


def fb_kwin2pdat(kwin, ds):
    if kwin == 3:
        xd = ds['pwin9']
    elif kwin == 1:
        xd = ds['pdraw9']
    elif kwin == 0:
        xd = ds['plost9']
    #
    return xd


def fb_gid_get4htm(htm):
    bs = BeautifulSoup(htm, 'html5lib')  # 'lxml'
    df = pd.DataFrame(columns=tfsys.gidSgn, dtype=str)
    ds = pd.Series(tfsys.gidNil, index=tfsys.gidSgn, dtype=str)

    # ---1#
    zsys.bs_get_ktag_kstr = 'isend'
    x10 = bs.find_all(zweb.bs_get_ktag)
    for xc, x in enumerate(x10):
        # print('\n@x\n',xc,'#',x.attrs)
        ds['gid'], ds['gset'] = x['fid'], zstr.str_fltHtmHdr(x['lg'])
        ds['mplay'] = zstr.str_fltHtmHdr(x['homesxname'])
        ds['gplay'] = zstr.str_fltHtmHdr(x['awaysxname'])
        ds['kend'] = x['isend']
        s2 = ds['tweek'] = x['gdate'].split(' ')[0]  # tweek
        ds['tweek'] = fb_tweekXed(s2)
        ds['tplay'], ds['tsell'] = x['pdate'], x['pendtime']  # tplay,tsell,
        #
        df = df.append(ds.T, ignore_index=True)

    # ---2#
    x20 = bs.find_all('a', class_='score')
    for xc, x in enumerate(x20):
        xss = x['href']
        kss = zstr.str_xmid(xss, 'ju-', '.sh')
        clst = x.text.split(':')
        #
        ds = df[df['gid'] == kss]
        ds = df[df['gid'] == kss]
        if len(ds) == 1:
            inx = ds.index
            df['qj'][inx] = clst[0]
            df['qs'][inx] = clst[1]
            kwin = fb_kwin4qnum(int(clst[0]), int(clst[1]))
            df['kwin'][inx] = str(kwin)

    # ---3#
    x20 = bs.find_all('td', class_='left_team')
    if (len(x20) == len(x10)):
        for xc, x in enumerate(x20):
            # print('@x',xc,'#',x.a['href'])
            xss = x.a['href']
            if xss.find('/team//') < 0:
                xid = zstr.str_xmid(xss, '/team/', '/')
                df['mtid'][xc] = xid
                g01 = df['gid'][xc]
                if xid == '':
                    zt.f_addLog('tid-mtid,nil,' + xss + ',gid,' + g01)
    # ---4#
    x20 = bs.find_all('td', class_='right_team')
    if (len(x20) == len(x10)):
        for xc, x in enumerate(x20):
            # print('@x',xc,'#',x.a['href'])
            xss = x.a['href']
            if xss.find('/team//') < 0:
                xid = zstr.str_xmid(xss, '/team/', '/')
                df['gtid'][xc] = xid
                g01 = df['gid'][xc]
                if xid == '':
                    zt.f_addLog('tid-gtid,nil,' + xss + ',gid,' + g01)

    # ---5#
    df = df[df['gid'] != '-1']
    return df


def fb_gid_getExt_oz4clst(ds, clst):
    i = 0
    ds['pwin0'], ds['pdraw0'], ds['plost0'] = clst[i], clst[i + 1], clst[i + 2]
    i = i + 3
    ds['pwin9'], ds['pdraw9'], ds['plost9'] = clst[i], clst[i + 1], clst[i + 2]
    i = i + 3
    ds['vwin0'], ds['vdraw0'], ds['vlost0'] = clst[i], clst[i + 1], clst[i + 2]
    i = i + 3
    ds['vwin9'], ds['vdraw9'], ds['vlost9'] = clst[i], clst[i + 1], clst[i + 2]
    i = i + 3
    ds['vback0'], ds['vback9'] = clst[i], clst[i + 1]
    i = i + 2
    ds['vwin0kali'], ds['vdraw0kali'], ds[
        'vlost0kali'] = clst[i], clst[i + 1], clst[i + 2]
    i = i + 3
    ds['vwin9kali'], ds['vdraw9kali'], ds[
        'vlost9kali'] = clst[i], clst[i + 1], clst[i + 2]
    #
    return ds


def fb_gid_getExt_oz4htm(htm, bars, ftg=''):
    bs = BeautifulSoup(htm, 'html5lib')  # 'lxml'
    x10 = bs.find_all('tr', ttl='zy')
    df = pd.DataFrame(columns=tfsys.gxdatSgn)
    ds = pd.Series(tfsys.gxdatNil, index=tfsys.gxdatSgn)
    xc, gid = 0, bars['gid']
    xlst = ['gset', 'mplay', 'mtid', 'gplay', 'gtid', 'qj',
            'qs', 'qr', 'kwin', 'kwinrq', 'tplay', 'tweek']
    for xc, x in enumerate(x10):
        # print('\n@x\n',xc,'#',x.attrs)
        x2 = x.find('td', class_='tb_plgs')  # print(x2.attrs)
        ds['gid'], ds['cid'], ds['cname'] = gid, x['id'], x2['title']
        #
        x20 = x.find_all('table', class_='pl_table_data')
        clst = zt.lst4objs_txt(x20, ['\n', '\t', '%'])
        ds = fb_gid_getExt_oz4clst(ds, clst)
        #
        zdat.df_2ds8xlst(bars, ds, xlst)
        df = df.append(ds.T, ignore_index=True)

    #
    # print('xx',xc)
    # --footer
    if xc > 0:
        x10 = bs.find_all('tr', xls='footer')

        for xc, x in enumerate(x10):
            # print('\n@x\n',xc,'#',x.attrs)
            if xc < 3:
                x20 = x.find_all('table', class_='pl_table_data')
                clst = zt.lst4objs_txt(x20, ['\n', '\t', '%'])
                ds['gid'] = gid
                if xc == 0:
                    ds['cid'], ds['cname'] = '90005', 'gavg'
                if xc == 1:
                    ds['cid'], ds['cname'] = '90009', 'gmax'
                if xc == 2:
                    ds['cid'], ds['cname'] = '90001', 'gmin'
                #
                zdat.df_2ds8xlst(bars, ds, xlst)
                ds = fb_gid_getExt_oz4clst(ds, clst)
                #
                df = df.append(ds.T, ignore_index=True)
        #
        if ftg != '':
            df.to_csv(ftg, index=False)
    #
    return df


def fb_gid_getExt010(x10):
    bars = pd.Series(x10, index=tfsys.gidSgn, dtype=str)
    gid = bars['gid']
    #
    fss = tfsys.rhtmOuzhi + gid + '_oz.htm'
    uss = tfsys.us0_extOuzhi + gid + '.shtml'  # print(uss)
    # zt.zt_web_get001txtFg or(fsiz<5000):
    htm = zweb.web_get001txtFg(uss, fss)
    #
    fxdat = tfsys.rxdat + gid + '_oz.dat'
    fsiz = zt.f_size(fxdat)  # print(zsys.sgnSP4,'@',fsiz,fxdat)
    #
    # print('xtfb.bars',xtfb.bars)
    if (fsiz < 1000) or (tfsys.xnday_down < 10):
        fb_gid_getExt_oz4htm(htm, bars, ftg=fxdat)

    '''
    #
    fss=xtfb.rhtmYazhi+xtfb.kgid+'_az.htm'
    uss=xtfb.us0_extYazhi+xtfb.kgid+'.shtml'
    #
    fss=xtfb.rhtmShuju+xtfb.kgid+'_sj.htm'
    uss=xtfb.us0_extShuju+xtfb.kgid+'.shtml'
    '''

    return fxdat


def fb_gid_getExt(df):
    dn9 = len(df['gid'])
    for i, row in df.iterrows():
        # xtfb.kgid=row['gid']
        # xtfb.bars=row
        fb_gid_getExt010(row.values)
        #
        print(zsys.sgnSP8, i, '/', dn9, '@ext')


def fb_gid_getExtPool(df, nsub=5):
    pool = ThreadPoolExecutor(max_workers=nsub)
    xsubs = [pool.submit(fb_gid_getExt010, x10) for x10 in df.values]
    #
    dn9 = len(df['gid'])
    ns9 = str(dn9)
    for xsub in as_completed(xsubs):
        fss = xsub.result(timeout=20)
        print('@_getExtPool,xn9:', ns9, fss)


def fb_gid_get_nday(xtfb, timStr, fgExt=False):
    if not timStr:
        ktim = xtfb.tim_now
    else:
        ktim = arrow.get(timStr)
    #
    nday = tfsys.xnday_down
    for tc in range(0, nday):
        xtim = ktim.shift(days=-tc)
        xtimStr = xtim.format('YYYY-MM-DD')
        # print('\nxtim',xtim,xtim<xtfb.tim0_gid)
        #
        xss = str(tc) + '#,' + xtimStr + ',@' + zt.get_fun_nam()
        zt.f_addLog(xss)
        if xtim < xtfb.tim0_gid:
            print('#brk;')
            break
        #

        fss = tfsys.rghtm + xtimStr + '.htm'
        uss = tfsys.us0_gid + xtimStr
        print(timStr, tc, '#', fss)
        #
        htm = zweb.web_get001txtFg(uss, fss)
        if len(htm) > 5000:
            df = fb_gid_get4htm(htm)
            if len(df['gid']) > 0:
                tfsys.gids = tfsys.gids.append(df)
                tfsys.gids.drop_duplicates(
                    subset='gid', keep='last', inplace=True)
                if fgExt:
                    fb_gid_getExtPool(df)
    #
    if tfsys.gidsFN:
        print('')
        print(tfsys.gids.tail())
        tfsys.gids.to_csv(tfsys.gidsFN, index=False)


def fb_xdat_xrd020(fsr, xlst, ysgn='kwin', k0=1, fgPr=False):
    # 1
    df = pd.read_csv(fsr, index_col=False)
    # 2
    if ysgn == 'kwin':
        df[ysgn] = df[ysgn].astype(str)
        df[ysgn].replace('3', '2', inplace=True)
    # 3
    df[ysgn] = df[ysgn].astype(float)
    df[ysgn] = round(df[ysgn] * k0).astype(int)
    # 4
    x_dat, y_dat = df[xlst], df[ysgn]

    # 5
    if fgPr:
        print('\n', fsr)
        print('\nx_dat')
        print(x_dat.tail())
        print('\ny_dat')
        print(y_dat.tail())
        # df.to_csv('tmp\df.csv',index=False)
    # 6
    return x_dat, y_dat


def fb_xdat_xlnk(rs0, ftg):
    flst = zt.lst4dir(rs0)
    df9 = pd.DataFrame(columns=tfsys.gxdatSgn, dtype=str)
    for xc, fs0 in enumerate(flst):
        fss = rs0 + fs0
        print(xc, fss)
        df = pd.read_csv(fss, index_col=False, dtype=str)
        #
        df2 = df[df['kwin'] != '-1']
        df9 = df9.append(df2, ignore_index=True)
        #
        if (xc % 2000) == 0:
            # df9.to_csv(ftg,index=False)
            fs2 = 'tmp/x_' + str(xc) + '.dat'
            print(fs2, fss)
            df9.to_csv(fs2, index=False)
    #
    df9.to_csv(ftg, index=False)
