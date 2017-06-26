# coding: utf-8
'''
由从文件读取数据改为直接读取网页
'''
import urllib2

from bs4 import BeautifulSoup


def bs010(fsr):
    bs = BeautifulSoup(fsr, 'lxml')  # 'lxml'
    # print('\n@ bs.type #1')
    # print('\ntype:bs,', type(bs))
    # print('\ntype:bs.title,', type(bs("title").text()), '\n', bs("title").text())
    print('\ntype:bs.title,', type(bs.title), '\n', bs.title)
    print('\ntype:bs.title.name,', type(bs.title.name), '\n', bs.title.name)
    print('\ntype:bs.title.attrs,', type(bs.title.attrs), '\n', bs.title.attrs)
    print('\ntype:bs.title.string,', type(bs.title.string), '\n', bs.title.string)
    print('\ntype:bs.title.strings,', type(bs.title.strings), '\n', bs.title.strings)

    print('\n\n@ bs.type #2')
    print('\ntype:bs.a,', type(bs.a), '\n', bs.a)
    print('\ntype:bs.a.name,', type(bs.a.name), '\n', bs.a.name)
    print('\ntype:bs.a.attrs,', type(bs.a.attrs), '\n', bs.a.attrs)

    print('\n\n@ bs #3')
    print('type:bs.a["class"],', type(bs.a['class']), bs.a['class'])
    print('bs.a["rel"],', bs.a['rel'])
    print('bs.a["target"],', bs.a['target'])
    print('bs.a["href"],', bs.a['href'])
    print('type:bs.a["data_tongji"],', bs.a['data_tongji'])

    print('\n\n@ bs #4')
    print('bs.a.get("class"),', bs.a.get('class'))
    print('bs.a.get("rel"),', bs.a.get('rel'))
    print('bs.a.get("target"),', bs.a.get('target'))
    print('bs.a.get("href"),', bs.a.get('href'))
    print('bs.a.get("data_tongji"),', bs.a.get('data_tongji'))

    print('\n\n@ bs #5')
    print('type:bs.name,', type(bs.name))
    print('bs.name,', bs.name)
    print('bs.attrs,', bs.attrs)
    print('bs.string,', bs.string)
    print('bs.strings,', bs.strings)


# -----------------------
# fss = 'tmp/500_2017-06-24.htm'
# fss = 'tmp/500_2017-06-23.htm'
# fss = 'tmp/500_2017-06-19.htm'
# fss = 'tmp/500_2010-01-01.htm'
# fss = 'dat/500_2010-01-01.htm'
# print('f,', fss)

_date_2010 = '2010-01-02'
# _date_2010 = '2010-01-01'
url_pre = 'http://trade.500.com/jczq/?date='
url = url_pre + _date_2010
request = urllib2.Request(url)
response = urllib2.urlopen(request)
html_doc = response.read()
bs010(html_doc)
