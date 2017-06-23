# coding=utf-8
'''
获取排列前10名的比赛次数
'''

import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from zsys import cors_brg, gid_file
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def gid_anz_top10(df, column):
    total_numbers = len(df['gid'])
    # 获取俱乐部排名前10,依据比赛次数从大到小排列
    d10 = df[column].value_counts()[:10]
    # print(d10)

    # mpl.rcParams['font.sans-serif'] = ['STHeiti-Light.ttc']  # 指定默认字体
    mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
    # 以上是一种方式，还有一种改变的方式https://segmentfault.com/a/1190000005144275或者
    # http://wenda.chinahadoop.cn/question/5304
    # help(d10.plot)
    # 柱状图
    d10.plot(kind='bar', rot=0, color=cors_brg)
    plt.show()
    #
    d10_sum = d10.sum()
    d10['other'] = total_numbers - d10_sum

    # d10是一个pandas对象
    k10 = np.round(d10 / total_numbers * 100, decimals=2)
    # print(k10)

    k10.plot(kind='pie', rot=0, table=True)
    plt.show()


# rs0 = './'
# fgid = rs0 + 'gid2017.dat'
df = pd.read_csv(gid_file, index_col=False, dtype=str)
gid_anz_top10(df, 'gset')
