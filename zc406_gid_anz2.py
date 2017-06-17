# coding=utf-8
'''
比赛数据年度图表分析
'''
import pandas as pd


def dr_gid_tim(df, ksgn, xlst):
    xdf = pd.DataFrame(columns=['nam', 'dnum'])
    ds = pd.Series(['', 0], index=['nam', 'dnum'])
    for xtim in xlst:
        xtim0, xtim9 = xtim + '-01-01', xtim + '-12-31'
        df2 = df[xtim0 <= df['tplay']]
        # print('\nx0',xtim,len(df2['gid']));#print(df2.tail())
        df3 = df2[df2['tplay'] <= xtim9]
        # print('x9',xtim,len(df3['gid']));#print(df3.tail())
        ds['nam'], ds['dnum'] = xtim, len(df3[ksgn])
        xdf = xdf.append(ds.T, ignore_index=True)
    #
    xdf.index = xdf['nam']
    print(xdf)
    xdf.plot(kind='bar', rot=0)


rs0 = './'
fgid = rs0 + 'gid2017.dat'
df = pd.read_csv(fgid, index_col=False, dtype=str)
print df.head()
#
xlst = ['2010', '2011', '2012', '2013', '2014', '2015', '2016']
dr_gid_tim(df, 'gid', xlst)
