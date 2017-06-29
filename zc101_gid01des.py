# coding=utf-8
'''
获取排列前10名的比赛次数
'''

import pandas as pd
from zsys import gid_file
from tfb_tools import gid_anz_top10
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# rs0 = './'
# fgid = rs0 + 'gid2017.dat'
# gid_file 是已手机的数据合并成的
df = pd.read_csv(gid_file, index_col=False, dtype=str)
# 获取俱乐部排名前10,依据比赛次数从大到小排列
gid_anz_top10(df, 'gset')
