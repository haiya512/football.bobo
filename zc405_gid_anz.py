# coding=utf-8
'''

'''
import pandas as pd
import tfb_tools as tft
import tfb_draw as tfdr

rs0 = './'
fgid = rs0 + 'gid2017.dat'
df = pd.read_csv(fgid, index_col=False, dtype=str)
tft.fb_df_type_xed(df)
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
print('\nok,!')
