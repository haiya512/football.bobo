# coding: utf-8
'''
提取球队比赛未开奖之前的数据
这个脚本暂时没有写获取mtid和gtid
'''
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
        ds['gset'] = zstr.str_fltHtmHdr(x['lg'])
        ds['gid'] = x['fid']
        ds['mplay'] = zstr.str_fltHtmHdr(x['homesxname'])
        # ds['mtid'] = x['mid']
        ds['mtid'] = 'NAN'
        ds['gplay'] = zstr.str_fltHtmHdr(x['awaysxname'])
        ds['gtid'] = 'NAN'
        ds['kend'] = x['isend']
        ds['tweek'] = x['gdate'].split(' ')[0]
        ds['tplay'] = x['pendtime']
        ds['tsell'] = x['pdate']

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
url_pre = 'http://trade.500.com/jczq/?date='
for date in ['2017-06-29', '2017-06-30']:
    # _date_2010 = '2017-06-29'
    # _date_2010 = '2010-01-01'
    url = url_pre + date
    print(url)
    # request = urllib2.Request(url)
    # response = urllib2.urlopen(request)
    # html_doc = response.read()
    html_doc = web_get001(url)

    df = gid_get001(html_doc)
    # print('')
    # print(df)
    # print(df.tail())
    df.to_csv('tmp/gid0629_0630.csv', index=False, mode='a', encoding='utf-8')
