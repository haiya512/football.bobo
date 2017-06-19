# coding=utf-8

import pandas as pd
import ztools_tst as ztst
import tfb_draw as tfdr

rs0 = './'
# rs0 = '/tfbdat/'
fgid = rs0 + 'gid2017.dat'
df = pd.read_csv(fgid, index_col=False, dtype=str)


@ztst.fun_tim01
def df_get8tim(df, ksgn, kpre, kn9, kpos):
    xdf = pd.DataFrame(columns=['nam', 'dnum'])
    ds = pd.Series(['', 0], index=['nam', 'dnum'])
    for xc in range(1, kn9 + 1):
        xss, kss = '{0:02d}'.format(xc), '{0}{1:02d}'.format(kpre, xc)
        df2 = df[df[ksgn].str.find(kss) == kpos]
        ds['nam'], ds['dnum'] = xss, len(df2['gid'])
        xdf = xdf.append(ds.T, ignore_index=True)
        # print(xc,'#',xss,kss)
    #
    xdf.index = xdf['nam']
    return xdf


ksgn = 'tplay'
xdf = df_get8tim(df, ksgn, '-', 12, 4)

tfdr.dr_gid_top10(df, 'kwin')
print('\nok,!')
