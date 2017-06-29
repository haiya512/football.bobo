# coding: utf-8
'''
显示比赛总数前10名的球队，还有他们的球队比赛数占比
'''
import pandas as pd
from zsys import gid_file
from tfb_tools import gid_anz_top10


# fgid = 'gid2017.dat'
df = pd.read_csv(gid_file, index_col=False, dtype=str)
print(df.tail())
print('\n', df.describe())
gid_anz_top10(df, 'gset')
