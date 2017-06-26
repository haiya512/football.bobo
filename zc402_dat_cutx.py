# coding=utf-8
'''
批量切割数据文件脚本
'''
import pandas as pd
from ztools_data import df_kcut8yearlst
from zsys import xdat_file, gid_file


gids = pd.read_csv(gid_file, index_col=False, dtype=str)
xdats = pd.read_csv(xdat_file, index_col=False, dtype=str)
#
ksgn = 'tplay'
yearlist = ['2010', '2011', '2012', '2013', '2014', '2015', '2016']
#
# gid_filename_pre = 'tmp/gidx_'
# df_kcut8yearlst(gids, ksgn, gid_filename_pre, yearlist)
#
# xd_filename_pre = 'tmp/xd_'
# df_kcut8yearlst(xdats, ksgn, xd_filename_pre, yearlist)

for file_pre in ['tmp/gidx_', 'tmp/xd_']:
    df_kcut8yearlst(gids, ksgn, file_pre, yearlist)