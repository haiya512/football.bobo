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
from ztools import maxium_fun, score_kwin_result


def gid_get001(htm, print_str=None):
    # bs = BeautifulSoup(htm, 'html5lib')  # 'lxml'
    bs = BeautifulSoup(htm, 'lxml')  # 'lxml'
    df = pd.DataFrame(columns=tfsys.gidSgn, dtype=str)
    ds = pd.Series(tfsys.gidNil, index=tfsys.gidSgn, dtype=str)

    # ---1#
    zsys.bs_get_ktag_kstr = 'isend'
    x10 = bs.find_all(zweb.bs_get_ktag)
    # print(x10)
    for xc, x in enumerate(x10):
        # print('\n@x\n', xc, '#', x.attrs)
        # print("x: ", x)
        # print("\n")
        sp_list = []
        # sp_nml_dict = {}
        # sp_rq_dict = {}
        ds['gset'] = zstr.str_fltHtmHdr(x['lg'])
        ds['gid'] = x['fid']
        ds['mplay'] = zstr.str_fltHtmHdr(x['homesxname'])
        # ds['mtid'] = x['mid']
        # ds['mtid'] = 'NAN'
        ds['gplay'] = zstr.str_fltHtmHdr(x['awaysxname'])
        ds['qr'] = x['rq']
        # ds['gtid'] = 'NAN'
        html_a = x.find_all(attrs={"class" :"score"})
        for _htmla in html_a:
            score_result = _htmla.text
            score_list = score_result.split(":")
            ds['mscore'] = score_list[0]
            # print("mscore: {0}".format(ds['mscore']))
            ds['pscore'] = score_list[1]
            # print("gscore: {0}".format(ds['pscore']))
            ds['kwin'] = score_kwin_result(ds['mscore'], ds['pscore'])
            ds['kwinrq'] = score_kwin_result(ds['mscore'], ds['pscore'], rq=ds['qr'])
            # print(ds['kwinrq'])

        html_span = x.find_all(attrs={"class": "odds_item"})
        for _htmlspan in html_span:
            # print(_htmlspan.attrs)
            # print("_htmlspan.text: {0}".format(_htmlspan.text))
            if str(_htmlspan.text) == u'\xa0':
                # print("_htmlspan.text is u' ' ")
                continue
            else:
                # print("_htmlspan.text is not u' ' ")
                sp_list.append(str(_htmlspan.text))
            # print(_htmlspan)
            # print("\n")
        # print(sp_list)
        # print("\n")
        ds['tsell'] = x['pdate']
        if len(sp_list) != 6:
            print("无法解析SP的比赛URL: {0} {1} {2} {3}".format(print_str,
                                                         ds['gset'],
                                                         ds['mplay'],
                                                         ds['gplay'],
                                                         ))
            continue
        ds['nml_win'] = nml_win = sp_list[0]
        ds['nml_draw'] = nml_draw = sp_list[1]
        ds['nml_lost'] = nml_lost = sp_list[2]
        ds['rq_win'] = rq_win = sp_list[3]
        ds['rq_draw'] = rq_draw = sp_list[4]
        ds['rq_lost'] = rq_lost = sp_list[5]

        sp_nml_dict = {
            3: nml_win,
            1: nml_draw,
            0: nml_lost,
        }

        sp_rq_dict = {
            3: rq_win,
            1: rq_draw,
            0: rq_lost,
        }
        # print(sp_nml_dict)
        ds['nml_sp_result'] = maxium_fun(sp_nml_dict)
        # print(maxium_fun(sp_nml_dict))
        ds['rp_sp_result'] = maxium_fun(sp_rq_dict)

        ds['kend'] = x['isend']
        if str(ds['kwin']) in ds['nml_sp_result']:
            ds['zhongjiang'] = True
        else:
            ds['zhongjiang'] = False
        if str(ds['kwinrq']) in ds['rp_sp_result']:
            ds['zhongjiang_rq'] = True
        else:
            ds['zhongjiang_rq'] = False
        # ds['tweek'] = x['gdate'].split(' ')[0]
        ds['tplay'] = x['pendtime']

        df = df.append(ds.T, ignore_index=True)

        # print(df)
    df = df[df['gid'] != '-1']
    return df


url_pre = 'http://trade.500.com/jczq/?date='
start_date = '2010-01-01'
# start_date = '2014-08-25'
# start_date = '2017-07-03'
end_date = '2017-07-07'
# end_date = '2010-01-02'
date_list = get_date_list(start_date, end_date)
# date_list = [end_date]
header = False
date_number = 0
for date in date_list:
    # _date_2010 = '2017-06-29'
    url = url_pre + date
    html_doc = web_get001(url)
    df = gid_get001(html_doc, url)
    if date_number == 0:
        header = True
    else:
        header = False
    date_number += 1
    if len(df.gid):
        # pass
        # gid_filename = 'gid/gid_' + date + '.csv'
        gid_filename = 'gid/gid_test.csv'
        # df.to_csv(gid_filename, index=False, encoding='utf-8', header=header)
        df.to_csv(gid_filename, index=False, encoding='utf-8', mode='a', header=header)
    else:
        print(url)
