# coding: utf-8
'''
演示栗子用
## 波波点评：
    没什么重要的作用
    一大堆的垃圾导入
    重复的计算时间
    演示了文件切割
'''

import pandas as pd
from zsys import xdat_file, gid_file
from ztools_data import df_kcut8tim


def fb_dat_cut(df, tim0str, tim9str):
    df2 = df[tim0str <= df['tplay']]
    df3 = df2[df2['tplay'] <= tim9str]
    return df3


# rs0 = './'
# gid_file = rs0 + 'gid2017.dat'
# xdat_file = rs0 + 'xdat2017.dat'
# tim0 = arrow.now()
# gids = pd.read_csv(gid_file, index_col=False, dtype=str)
# tim2 = arrow.now()
# t1 = zt.timNSec(tim2, tim0)
# 为了获取读文件gid2017.dat所耗费的时间
# print('rd gid2017 #1, ', t1)

xdats = pd.read_csv(xdat_file, index_col=False, dtype=str)
# tim2 = arrow.now()
# t1 = zt.timNSec(tim2, tim0)
# print(t1)
# # 为了获取读文件xdat2017.dat所耗费的时间
# print('rd xdat2017 #2, ', t1)

tim0str, tim9str = '2016-01-01', '2016-12-31'
xd2016 = fb_dat_cut(xdats, tim0str, tim9str)
# xd2016 = df_kcut8tim(xdats, 'tplay', tim0str, tim9str)
# tim2 = arrow.now()
# t1 = zt.timNSec(tim2, tim0)
# 仅仅是获取切割文件所用的时间
# print('cut xdat2016 #3, ', t1)
#
xd2016.to_csv('tmp/xd2016.dat', index=False)
# tim2 = arrow.now()
# t1 = zt.timNSec(tim2, tim0)
# print('wr xdat2016 #4, ', t1)
#
df2 = pd.read_csv('tmp/xd2016.dat', index_col=False)
# tim2 = arrow.now()
# t1 = zt.timNSec(tim2, tim0)
# print('rd xdat2016 #5, ', t1)
#
# print('\nxdat2016.tail() #6')
print(df2.tail(), '\n')

# tim2 = arrow.now().shift(days=2)
# t1, , t3 = zt.timNSec(tim2, tim0)
# t2 = zt.timNHour(tim2, tim0)
# t3 = zt.timNDay(tim2, tim0)
# print('s, h, d#9, ', t1, t2, t3)
