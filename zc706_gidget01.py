# coding=utf-8
'''
编写一个真正的商业级别的提取球队比赛数据的程序
'''
import urllib2

import pandas as pd
from bs4 import BeautifulSoup

import zsys
import ztools_str as zstr
import ztools_web as zweb
import tfb_sys as tfsys
from ztools_web import web_get001


def gid_get001(htm):
    # bs = BeautifulSoup(htm, 'html5lib')  # 'lxml'
    bs = BeautifulSoup(htm, 'lxml')  # 'lxml'
    df = pd.DataFrame(columns=tfsys.gidSgn, dtype=str)
    ds = pd.Series(tfsys.gidNil, index=tfsys.gidSgn, dtype=str)

    # ---1#
    zsys.bs_get_ktag_kstr = 'isend'
    x10 = bs.find_all(zweb.bs_get_ktag)
    for xc, x in enumerate(x10):
        print('\n@x\n', xc, '#', x.attrs)
        # print('\n@x\n',xc,'#',x.attrs)
        ds['gid'] = zstr.str_fltHtmHdr(x['lg'])
        ds['gset'] = x['fid']
        ds['mplay'] = zstr.str_fltHtmHdr(x['homesxname'])
        ds['gplay'] = zstr.str_fltHtmHdr(x['awaysxname'])
        ds['kend'] = x['isend']
        ds['tweek'] = x['gdate'].split(' ')[0]  # tweek
        ds['tplay'] = x['pendtime']  # tplay,tsell,
        ds['tsell'] = x['pdate']
        #
        df = df.append(ds.T, ignore_index=True)

    df = df[df['gid'] != '-1']
    return df


# fss = 'dat/500_2017-01-01.htm'
# print('f,', fss)
# hss = zt.f_rd(fss)
# df = gid_get001(hss)
# print('')
# print(df.tail())
# df.to_csv('tmp\gid01.csv', index=False, encoding='gbk')

_date_2010 = '2017-06-23'
# _date_2010 = '2010-01-01'
url_pre = 'http://trade.500.com/jczq/?date='
url = url_pre + _date_2010
# request = urllib2.Request(url)
# response = urllib2.urlopen(request)
# html_doc = response.read()
html_doc = web_get001(url)

df = gid_get001(html_doc)
# print('')
print(df)
# print(df.tail())
# df.to_csv('tmp\gid01.csv', index=False)
