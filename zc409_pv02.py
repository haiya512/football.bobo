# coding=utf-8
"""
生成图片并保存
"""

import pandas as pd
from tfb_draw import dr_gid_top10
from zsys import xdat_file

# rs0 = './'
# fdat = rs0 + 'xdat2017.dat'
# fdat='dat/xd_2016.dat'
df = pd.read_csv(xdat_file, index_col=False, dtype=str)
dfk = df[df['cid'] == '1']

xlst = ['pwin0', 'pdraw0', 'plost0', 'pwin9', 'pdraw9', 'plost9',
        'vwin0', 'vdraw0', 'vlost0', 'vwin9', 'vdraw9', 'vlost9',
        'vback0', 'vback9',
        'vwin0kali', 'vdraw0kali', 'vlost0kali', 'vwin9kali', 'vdraw9kali',
        'vlost9kali']

for ksgn in xlst:
    # print('\ndf', ksgn)
    dr_gid_top10(df, ksgn, 'tmp/' + ksgn + '_df_')
    # print('@dfk')
    dr_gid_top10(dfk, ksgn, 'tmp/' + ksgn + '_dk_')
