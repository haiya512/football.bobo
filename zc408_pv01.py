# coding: utf-8

import pandas as pd
import ztools_tst as ztst
from tfb_draw import dr_gid_top10
from zsys import gid_file

# rs0 = './'
# # rs0 = '/tfbdat/'
# fgid = rs0 + 'gid2017.dat'


@ztst.fun_tim01
def df_get8tim(df, ksgn=None, kpre=None, kn9=None, kpos=None):
    xdf = pd.DataFrame(columns=['nam', 'dnum'])
    ds = pd.Series(['', 0], index=['nam', 'dnum'])
    for xc in range(1, kn9 + 1):
        # 格式化生成月份数字
        xss = '{0:02d}'.format(xc)
        # 格式化生成如"-01"数字
        kss = '{0}{1:02d}'.format(kpre, xc)
        # print df[df[ksgn]]
        df2 = df[df[ksgn].str.find(kss) == kpos]
        ds['nam'] = xss
        ds['dnum'] = len(df2['gid'])
        xdf = xdf.append(ds.T, ignore_index=True)
        # print(xc,'#',xss,kss)
    #
    xdf.index = xdf['nam']
    return xdf

df = pd.read_csv(gid_file, index_col=False, dtype=str)

xdf = df_get8tim(df, ksgn='tplay', kpre='-', kn9=12, kpos=4)
# print xdf

dr_gid_top10(df, 'kwin')
