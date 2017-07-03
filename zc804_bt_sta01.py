# coding=utf-8
'''
这里定义的函数没有用,只是拷贝了一个一模一样的,所以删除
zc803的扩展
'''

# from tfb_main import main_bt
import zsys
import tfb_sys as tfsys
import tfb_tools as tft
import tfb_backtest as tfbt
import tfb_strategy as tfsty
from zsys import file_dir, gid_file
from ipython_debug import *


def main_bt(timStr='', nday=2):
    #
    # 1---init.sys
    # print('\nmain_bt,nday:', nday)
    tfsys.xnday_down = nday
    zsys.web_get001txtFg = True

    # 2---init.tfb
    # rs0 = './'
    # fgid = rs0 + 'gid2017.dat'
    xtfb = tft.fb_init(file_dir, gid_file)
    if nday == -1:
        tfsys.xnday_down = xtfb.gid_nday + 10
        print('nday,', tfsys.xnday_down)

    # 3---backtest
    # print('\n#3,backtest')
    if nday != 0:
        xtfb.funPre = tfsty.sta00_pre
        xtfb.funSta = tfsty.sta01_sta
        xtfb.preVars = []
        xtfb.staVars = [1.5]
        xtfb.kcid = '1'  # cn,3=bet365

        tfbt.bt_main(xtfb, timStr)

        # 4---main_ret
        # print('\n#4,result.anz')
        tfbt.bt_main_ret(xtfb, True)
        print('kcid,', xtfb.kcid, ',nday,', nday)
        print('preVar,', xtfb.preVars)
        print('staVar,', xtfb.staVars)


timeStr = '2017-01-05'  # 这个参数好像没卵用
# main_bt(timeStr, 5)
# def main_bt(timStr='', nday=2):
#
# 1---init.sys
# print('\nmain_bt,nday:', nday)
nday = 2
tfsys.xnday_down = nday
zsys.web_get001txtFg = True

# 2---init.tfb
rs0 = './'
fgid = rs0 + 'gid2017.dat'
xtfb = tft.fb_init(rs0, fgid)
if nday == -1:
    tfsys.xnday_down = xtfb.gid_nday + 10
    print('nday,', tfsys.xnday_down)

# 3---backtest
# print('\n#3,backtest')
if nday != 0:
    xtfb.funPre = tfsty.sta00_pre
    xtfb.funSta = tfsty.sta01_sta
    xtfb.preVars = []
    xtfb.staVars = [1.5]
    xtfb.kcid = '1'  # cn,3=bet365

    # set_trace()

    tfbt.bt_main(xtfb, timeStr)

    # set_trace()

    # 4---main_ret
    # print('\n#4,result.anz')
    tfbt.bt_main_ret(xtfb, True)
    print('kcid,', xtfb.kcid, ',nday,', nday)
    print('preVar,', xtfb.preVars)
    print('staVar,', xtfb.staVars)