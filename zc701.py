# coding=utf-8

import arrow
import ztools as zt
import ztools_web as zweb
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
#

# -----------------------
# ---1#
xtim = '2010-01-01'
us0 = 'http://trade.500.com/jczq/?date='
uss = us0 + xtim
fss = 'tmp/500_' + xtim + '_utf8.htm'
print('f,', fss)
rx = zweb.web_get001(uss)
htm = rx.text
zt.f_add(fss, htm, True, cod='utf-8')
#
# ---2#
fss = 'tmp/500_' + xtim + '_gbk.htm'
print('f,', fss)
# zt.f_add(fss, htm, True, cod='GBK')
zt.f_add(fss, htm, True)
#
# ---3#
fss = 'tmp/500_' + xtim + '.htm'
print('f,', fss)
zweb.web_get001txt(uss, ftg=fss)
#
# ---4#
xtim = arrow.now().format('YYYY-MM-DD')
uss = us0 + xtim
fss = 'tmp/500_' + xtim + '.htm'
print('f,', fss)
zweb.web_get001txt(uss, ftg=fss)
# ------------
#

print('\nok,完成!!')
