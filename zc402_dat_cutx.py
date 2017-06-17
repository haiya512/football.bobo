# coding=utf-8
'''
批量切割数据文件脚本
'''
import pandas as pd
import ztools_data as zdat


rs0 = './'
fgid, fdat = rs0 + 'gid2017.dat', rs0 + 'xdat2017.dat'
gids = pd.read_csv(fgid, index_col=False, dtype=str)
xdats = pd.read_csv(fdat, index_col=False, dtype=str)
#
ksgn = 'tplay'
ylst = ['2010', '2011', '2012', '2013', '2014', '2015', '2016']
#
ftg0 = 'tmp/gidx_'
zdat.df_kcut8yearlst(gids, ksgn, ftg0, ylst)
#
ftg0 = 'tmp/xd_'
zdat.df_kcut8yearlst(xdats, ksgn, ftg0, ylst)
