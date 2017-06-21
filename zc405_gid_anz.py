# coding=utf-8
'''
计算各关键字段前10名的占比并画图
'''
import pandas as pd
import tfb_tools as tft
import tfb_draw as tfdr

rs0 = './'
fgid = rs0 + 'gid2017.dat'
df = pd.read_csv(fgid, index_col=False, dtype=str)
tft.fb_df_type_xed(df)
# 为什么要计算进球数和失球数?
df['qsum'] = df['qj'] + df['qs']
print(df.tail())
draw_png_list = ['gset',
                 'mplay',
                 'qj',
                 'qs',
                 'qsum',
                 'tweek'
                 ]
for ele in draw_png_list:
    tfdr.dr_gid_top10(df, ele)
