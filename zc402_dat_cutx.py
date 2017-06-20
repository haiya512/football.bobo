# coding=utf-8
'''
批量切割数据文件脚本
'''
import pandas as pd
import ztools_data as zdat


rs0 = './'
fgid = rs0 + 'gid2017.dat'
fdat = rs0 + 'xdat2017.dat'
gids = pd.read_csv(fgid, index_col=False, dtype=str)
xdats = pd.read_csv(fdat, index_col=False, dtype=str)
#
ksgn = 'tplay'
yearlist = ['2010', '2011', '2012', '2013', '2014', '2015', '2016']
#
gid_filename_pre = 'tmp/gidx_'
zdat.df_kcut8yearlst(gids, ksgn, gid_filename_pre, yearlist)
#
xd_filename_pre = 'tmp/xd_'
zdat.df_kcut8yearlst(xdats, ksgn, xd_filename_pre, yearlist)
