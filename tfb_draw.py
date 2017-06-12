# -*- coding: utf-8 -*-

import bs4

import numpy as np

import matplotlib as mpl
from matplotlib import pyplot as plt

#import multiprocessing
#
#import arrow
import datetime as dt
import time
from dateutil.rrule import *
from dateutil.parser import *
import calendar as cal

#
import zsys


def dr_gid_top10(df, ksgn, ftg0=''):

    xn9 = len(df['gid'])
    d10 = df[ksgn].value_counts()[:10]
    print(d10)

    mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
    mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
    #
    d10.plot(kind='bar', rot=0, color=zsys.cors_brg)
    if ftg0 != '':
        plt.savefig(ftg0 + '_bar.png')
    plt.show()
    #
    dsum = d10.sum()
    d10['other'] = xn9 - dsum
    k10 = np.round(d10 / xn9 * 100, decimals=2)

    k10.plot(kind='pie', rot=0, table=True)
    if ftg0 != '':
        plt.savefig(ftg0 + '_pie.png')
    plt.show()
