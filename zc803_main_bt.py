# coding: utf-8
'''

'''
import zsys
import ztools as zt
import tfb_sys as tfsys
import tfb_tools as tft
import tfb_strategy as tfsty
import tfb_backtest as tfbt
from zsys import file_dir, gid_file


def main_bt(timeStr='', nday=2):
    tfsys.xnday_down = nday
    # 数据都已经获取了
    zsys.web_get001txtFg = True

    # rs0 = './'
    fgid = file_dir + gid_file
    xtfb = tft.fb_init(file_dir, fgid)
    if nday == -1:
        tfsys.xnday_down = xtfb.gid_nday + 10
        print('nday,', tfsys.xnday_down)

    if nday != 0:
        xtfb.funPre = tfsty.sta00_pre
        xtfb.funSta = tfsty.sta00_sta
        xtfb.preVars = []
        xtfb.staVars = []
        xtfb.kcid = '1'  # cn,3=bet365
        #
        tfbt.bt_main(xtfb, timeStr)
        tfbt.bt_main_ret(xtfb, True)
        print('kcid', xtfb.kcid)

    tn = zt.timNSec('', xtfb.tim0, '')
    print('\n#5,backtest,tim:{0:.2f} s'.format(tn))


# main_bt('', 2)
main_bt('', 100)
