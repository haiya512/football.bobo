# coding=utf-8
'''
毛用没有,就是看看读取文件花费的时间
'''

import arrow
import pandas as pd

import ztools as zt

rs0 = './'
fgid = rs0 + 'gid2017.dat'
fxdat = rs0 + 'xdat2017.dat'

tim0 = arrow.now()
gids = pd.read_csv(fgid, index_col=False, dtype=str)
tn = zt.timNSec('', tim0)
dn = len(gids.index)
print('#2,gids tim: {0}s,data num:{1:,} '.format(tn, dn))

# 3
tim0 = arrow.now()
xdats = pd.read_csv(fxdat, index_col=False, dtype=str)
tn = zt.timNSec('', tim0)
dn = len(xdats.index)
print('#3,xdats tim: {0}s,data num:{1:,} '.format(tn, dn))
