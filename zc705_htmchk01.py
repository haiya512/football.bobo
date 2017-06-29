# coding=utf-8
'''
不知道这个文件有什么用
'''
from bs4 import BeautifulSoup

import zsys
import ztools as zt
import ztools_web as zweb


def htm_chk001(htm):
    # bs = BeautifulSoup(htm, 'html5lib')  # 'lxml'
    bs = BeautifulSoup(htm, 'lxml')  # 'lxml'

    zsys.bs_get_ktag_kstr = 'isend'
    x10 = bs.find_all(zweb.bs_get_ktag)
    for xc, x in enumerate(x10):
        print('\n@x\n', xc, '#', x.attrs)


# fss = 'dat/500_2017-01-20.htm'
fss = 'dat/20170623.html'
print('f,', fss)
htm = zt.f_rd(fss)
# htm_chk001(hss)
# bs = BeautifulSoup(htm, 'html5lib')  # 'lxml'
bs = BeautifulSoup(htm, 'lxml')  # 'lxml'

zsys.bs_get_ktag_kstr = 'isend'
x10 = bs.find_all(zweb.bs_get_ktag)
for xc, x in enumerate(x10):
    print('\n@x\n', xc, '#', x.attrs)