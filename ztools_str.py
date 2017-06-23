# coding=utf-8
# -*- coding: utf-8 -*-
'''
Top极宽量化(原zw量化)，Python量化第一品牌
网站:www.TopQuant.vip   www.ziwang.com
QQ总群:124134140   千人大群 zwPython量化&大数据

TopQuant.vip ToolBox 2016
Top极宽·量化开源工具箱 系列软件
by Top极宽·量化开源团队 2016.12.25 首发

文件名:ztools_str.py
默认缩写：import ztools_str as zstr
简介：Top极宽字符串常用工具函数集
'''

import re

'''
str.misc.xxx
#
str_xpos
str.del.xxx
str.flt.xxx
#
pd.str.xxx  pandas
'''

def str_fnDay(cs0):
    mss = str(dt.date.today())
    xss = ''.join([cs0, '_', mss, '.dat'])
    return xss


def str_fn9xed(fs0, xs9):
    dss = fs0.split('.')[0]
    xss = ''.join([dss, xs9])
    return xss


# ----str.xpos.xxx
def str_l01(dss, kss):
    xc = s.find('.')
    return dss[:xc]


def str_r01(dss, kss):
    xc = s.rfind('.')
    return dss[xc + 1:]


def str_l01x(dss, kss):
    xc = s.find('.')
    return dss[:xc], dss[xc + 1:]


def str_r01x(dss, kss):
    xc = s.rfind('.')
    return dss[xc + 1:], dss[:xc]


def str_xmid(dss, ks1, ks9):
    # s="abcd232" ;x=str_xmid(s,'b','2');print(x)
    mx = ''.join(['(', ks1, ')(.*?)(', ks9, ')']);
    r = re.search(mx, dss)
    dat = ''
    if r: dat = r.groups()[1]
    return dat


def str_xor(dss, klst):
    # s="abcd232" ;x=str_xor(s,['b1','21','b']);print(x)
    if klst == None: return True
    #
    kss = '|'.join(klst)
    mx = ''.join(['(?:', kss, ')']);
    r = re.search(mx, dss)
    dat = (r != None)
    # print(dat)
    return dat


# def str_xand(dss,klst):

def str_mxrep(dstr, old_lst, new_lst):
    for xss, xs2 in zip(old_lst, new_lst):
        if dstr.find(xss) > -1:
            dstr = dstr.replace(xss, xs2)
    return dstr


# -------str.del.xxx
def str_del2cr(dss):
    while dss.find('\n\n') > -1:
        dss = dss.replace('\n\n', '\n')
    return dss


def str_del4sp(dss):
    sp4 = '    '
    while dss.find(sp4) > -1:
        dss = dss.replace(sp4, '  ')
    return dss


# -------str.flt.xxx
def str_flt(dss, xlst):
    for x in xlst:
        dss = dss.replace(x, '')
    return dss


def str_fltHtm(css):
    css = css.replace('\t', ' ')
    css = str_del2cr(css)
    css = str_del4sp(css)
    #
    return css


def str_fltHtmHdr(css):
    xlst = [' ', '（转）', '(转)', '组图', '(图)', '[转]', '[转载]', '【转】', '【转载】'
        , '&lt;', '&gt;', '&amp;', '&quot;', '&nbsp;', '　'
        , '-', '-', ',', '，', '?', '？', '!', '！', '(', ')', '[', ']', '/', '\\'
        , '#', '.', '、', '”', '“', '_', '（', '）', ':', '：', '【', '】', '「', '」', '《', '》']
    css = str_flt(css, xlst)  # ,''
    return css


# -----------------------

# ---pd.df.str.xxx
def df_strFind01(df, kss):
    xdf = df[df.str.find(kss) > -1]
    # print(xdf)
    xfg = len(xdf) > 0
    return xfg


def df_strFind(df, kss, colSgn):
    xdf = df[df[colSgn].str.find(kss) > -1]
    # print(xdf)
    xfg = len(xdf[colSgn]) > 0
    return xfg


# ---pd.df.flt.xxx
def df_fltHdr(df9):
    df9 = df9.drop_duplicates(['hdr'])
    df9 = df9.dropna()
    df9 = df9.sort_values('hdr')
    #
    return df9
