# coding: utf-8
'''
比赛场次年度数量的走势
'''
import pandas as pd
import matplotlib.pyplot as plt
from zsys import gid_file


def dr_gid_tim(df, year_list):
    xdf = pd.DataFrame(columns=['nam', 'dnum'])
    ds = pd.Series(['', 0], index=['nam', 'dnum'])
    for xtim in year_list:
        xtim0 = xtim + '-01-01'
        xtim9 = xtim + '-12-31'
        df2 = df[xtim0 <= df['tplay']]
        df3 = df2[df2['tplay'] <= xtim9]
        ds['nam'] = xtim
        ds['dnum'] = len(df3['tplay'])
        xdf = xdf.append(ds.T, ignore_index=True)
    xdf.index = xdf['nam']
    # print(xdf)
    xdf.plot(kind='bar', rot=0)
    plt.show()


# rs0 = './'
# fgid = rs0 + 'gid2017.dat'
df = pd.read_csv(gid_file, index_col=False, dtype=str)
# print df.head()
#
year_list = ['2010', '2011', '2012', '2013', '2014', '2015', '2016']
dr_gid_tim(df, year_list)
