# coding: utf-8
'''
Created on 2016.12.25
Top Football
Top Quant for football-极宽足彩量化分析系统
简称TFB，培训课件-配套教学python程序
@ www.TopQuant.vip      www.ziwang.com
'''
import os
import re
import pandas as pd
import numpy as np
import arrow

import requests
import bs4
from bs4 import BeautifulSoup
from robobrowser import RoboBrowser

import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib.colors
from matplotlib import cm

import zsys
import ztools as zt
import zpd_talib as zta
#
import tfb_sys as tfsys
import tfb_tools as tft
# -----------------------

# -----------------------


def gid_anz_top10(df, ksgn):
    xn9 = len(df['gid'])
    d10 = df[ksgn].value_counts()[:10]
    print(d10)
    # ---set chinese font
    # mpl.rcParams['font.sans-serif'] = ['SimHei']
    # 指定默认字体
    mpl.rcParams['axes.unicode_minus'] = False
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
rs0 = '/tfbDat/'
fgid = rs0 + 'gid2017.dat'
df = pd.read_csv(fgid, index_col=False, dtype=str, encoding='gbk')
print(df.tail())
print('\n', df.describe())
#
gid_anz_top10(df, 'gset')
# ------------
#
print('\nok, !')
