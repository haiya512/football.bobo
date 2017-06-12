# coding=utf-8
'''
获取排列前10名的比赛次数
'''
import sys
import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
import zsys
reload(sys)
sys.setdefaultencoding('utf-8')


def gid_anz_top10(df, ksgn):
    xn9 = len(df['gid'])
    d10 = df[ksgn].value_counts()[:10]
    print(d10)

    # mpl.rcParams['font.sans-serif'] = ['STHeiti-Light.ttc']  # 指定默认字体
    mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
    # 以上是一种方式，还有一种改变的方式https://segmentfault.com/a/1190000005144275或者
    # http://wenda.chinahadoop.cn/question/5304
    # help(d10.plot)
    # 柱状图
    d10.plot(kind='bar', rot=0, color=zsys.cors_brg)
    plt.show()
    #
    dsum = d10.sum()
    d10['other'] = xn9 - dsum
    k10 = np.round(d10 / xn9 * 100, decimals=2)

    k10.plot(kind='pie', rot=0, table=True)
    plt.show()


rs0 = './'
fgid = rs0 + 'gid2017.dat'
df = pd.read_csv(fgid, index_col=False, dtype=str)
# print(df.tail())
# print('\n', df.describe())
#
gid_anz_top10(df, 'gset')
print('\nok,!')
