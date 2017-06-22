# coding: utf-8

"""
很好奇,这个文件是以网站名字开头的,那么怎么合成gid和xdat呢?
数据是不是合成这两个文件需要的呢?
"""

import arrow
import ztools as zt
# from ztools import zt_headers
from ztools_web import zt_headers
import ztools_web as zweb
import requests
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

_date_2010 = '2010-01-01'
url_pre = 'http://trade.500.com/jczq/?date='
url = url_pre + _date_2010
file_name = 'tmp/500_' + _date_2010 + '_utf8.htm'
rx = zweb.web_get001(url)
rx_new = requests.get(url, headers=zt_headers)
try:
    html_content = rx.text
    zt.f_add(file_name, html_content, create_file=True, encode='utf-8')
except:
    print("Error: get 2010-01-01 500 ")

today = arrow.now().format('YYYY-MM-DD')

today_url = url_pre + today
file_name = 'tmp/500_' + today + '.htm'
print('filename: ', file_name)
zweb.web_get001txt(today_url, filename=file_name)
