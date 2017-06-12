# coding: utf-8
'''

'''
import pandas as pd
import numpy as np
# import matplotlib as mpl
from matplotlib import pyplot as plt
import zsys
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def gid_anz_top10(df, ksgn):
    xn9 = len(df['gid'])
    d10 = df[ksgn].value_counts()[:10]
    print(d10)
    # ---set chinese font
    # mpl.rcParams['font.sans-serif'] = ['SimHei']
    # 指定默认字体
    # mpl.rcParams['axes.unicode_minus'] = False
    # 解决保存图像是负号'-'显示为方块的问题
    d10.plot(kind='bar', rot=0, color=zsys.cors_brg)
    plt.show()
    #
    dsum = d10.sum()
    d10['other'] = xn9 - dsum
    k10 = np.round(d10 / xn9 * 100, decimals=2)

    k10.plot(kind='pie', rot=0, table=True)
    plt.show()


# -----------------------
rs0 = './'
fgid = rs0 + 'gid2017.dat'
df = pd.read_csv(fgid, index_col=False, dtype=str)
print(df.tail())
print('\n', df.describe())
gid_anz_top10(df, 'gset')
# ------------
#
print('\nok, !')
