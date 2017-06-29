# coding: utf-8

"""
很好奇,这个文件是以网站名字开头的,那么怎么合成gid和xdat呢?
数据是不是合成这两个文件需要的呢?
获取 2010-01-02和今天的比赛数据
主要就是介绍ztools_web.web_get001txt 的使用方法
"""

import arrow

from ztools import f_add

# from ztools import zt_headers
from ztools_web import zt_headers
from ztools_web import web_get001, web_get001txt
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

# _date_2010 = '2017-06-23'
_date_2010 = '2010-01-02'
# _date_2010 = '2010-01-01'
url_pre = 'http://trade.500.com/jczq/?date='
url = url_pre + _date_2010
# file_name = 'tmp/500_' + _date_2010 + '_utf8.htm'
file_name = 'tmp/500_' + _date_2010 + '.htm'
print file_name

html_content = web_get001(url)
# rx_new = requests.get(url, headers=zt_headers)
try:
    f_add(file_name, html_content)
except:
    print("Error: get 2010-01-01 500 ")

today = arrow.now().format('YYYY-MM-DD')
today_url = url_pre + today
file_name = 'tmp/500_' + today + '.htm'
print file_name
# print('filename: ', file_name)
web_get001txt(today_url, filename=file_name)
