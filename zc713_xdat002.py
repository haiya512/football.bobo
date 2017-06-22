# coding=utf-8
'''
不好不好,gid是定死的,只能查询一个
'''

import pandas as pd
from bs4 import BeautifulSoup
import ztools as zt
import ztools_data as zdat
import tfb_sys as tfsys
import tfb_tools as tft


def fb_gid_getExt_oz4htm(htm, bars, ftg=''):
    bs = BeautifulSoup(htm, 'html5lib')
    x10 = bs.find_all('tr', ttl='zy')
    df = pd.DataFrame(columns=tfsys.gxdatSgn)
    ds = pd.Series(tfsys.gxdatNil, index=tfsys.gxdatSgn)
    xc = 0
    gid = bars['gid']
    xlst = ['gset', 'mplay', 'mtid', 'gplay', 'gtid', 'qj', 'qs', 'qr', 'kwin', 'kwinrq', 'tplay', 'tweek']
    for xc, x in enumerate(x10):
        # print('\n@x\n',xc,'#',x.attrs)
        x2 = x.find('td', class_='tb_plgs')
        ds['gid'], ds['cid'], ds['cname'] = gid, x['id'], x2['title']
        #
        x20 = x.find_all('table', class_='pl_table_data');
        clst = zt.lst4objs_txt(x20, ['\n', '\t', '%'])
        ds = tft.fb_gid_getExt_oz4clst(ds, clst)
        #
        zdat.df_2ds8xlst(bars, ds, xlst)
        df = df.append(ds.T, ignore_index=True)

    # print('xx',xc)

    if xc > 0:
        x10 = bs.find_all('tr', xls='footer')

        for xc, x in enumerate(x10):
            # print('\n@x\n',xc,'#',x.attrs)
            if xc < 3:
                x20 = x.find_all('table', class_='pl_table_data')
                clst = zt.lst4objs_txt(x20, ['\n', '\t', '%'])
                ds['gid'] = gid
                if xc == 0: ds['cid'], ds['cname'] = '90005', 'gavg'
                if xc == 1: ds['cid'], ds['cname'] = '90009', 'gmax'
                if xc == 2: ds['cid'], ds['cname'] = '90001', 'gmin'
                #
                zdat.df_2ds8xlst(bars, ds, xlst)
                ds = tft.fb_gid_getExt_oz4clst(ds, clst)
                #
                df = df.append(ds.T, ignore_index=True)
        #
        if ftg:
            # df.to_csv(ftg, index=False, encoding='gb18030')
            df.to_csv(ftg, index=False)
    return df


gid = '240228'
fgid = './gid2017.dat'
gids = pd.read_csv(fgid, index_col=False, dtype=str)

g10 = gids[gids['gid'] == gid]

bars = pd.Series(list(g10.values[0]), index=list(g10))
# print('\n#2')
# print(bars)
# print('\ntype(g10),', type(g10))

fhtm = 'dat/' + gid + '_oz.htm'
ftg = 'tmp/' + gid + '_xd.dat'
# 读取文件内容
htm = zt.f_rd(fhtm)
df = fb_gid_getExt_oz4htm(htm, bars, ftg)
# print('\n#3')
print(df.tail())
