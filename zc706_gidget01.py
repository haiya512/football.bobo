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
from tfb_tools import get_date_list


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


url_pre = 'http://trade.500.com/jczq/?date='
start_date = '2010-01-01'
end_date = '2017-07-04'
date_list = get_date_list(start_date, end_date)
# for date in ['2017-06-29', '2017-06-30']:
# date_list = ['2015-06-23', '2016-06-27']
header = False
date_number = 0
for date in date_list:
    # _date_2010 = '2017-06-29'
    # _date_2010 = '2010-01-01'
    url = url_pre + date
    html_doc = web_get001(url)
    df = gid_get001(html_doc)
    if date_number == 0:
        header = True
    else:
        header = False
    date_number += 1
    if len(df.gid):
        gid_filename = 'gid/gid_' + date + '.csv'
        # gid_filename = 'gid/gid_test.csv'
        df.to_csv(gid_filename, index=False, encoding='utf-8', mode='a', header=header)
    else:
        print(url)
