# -*- coding: utf-8 -*-
import numpy as np
# import matplotlib as mpl
from matplotlib import pyplot as plt
# import multiprocessing
# import arrow
import zsys
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def dr_gid_top10(df, column, title=None, save=False):
    """
    column: 要传入的列名
    png_name: 图片的名称
    """

    xn9 = len(df['gid'])
    d10 = df[column].value_counts()[:10]
    print(d10)

    # mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
    # mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
    #
    d10.plot(kind='bar', rot=0, color=zsys.cors_brg)
    if title:
        plt.savefig(title + '_bar.png')
    plt.show()
    #
    dsum = d10.sum()
    d10['other'] = xn9 - dsum
    k10 = np.round(d10 / xn9 * 100, decimals=2)

    k10.plot(kind='pie', rot=0, table=True)
    if title:
        plt.savefig(title + '_pie.png')
    plt.show()
