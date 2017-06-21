# coding=utf-8
'''
策略sta01  sta是strategy的缩写

'''
import zsys
import ztools as zt
import tfb_sys as tfsys
import tfb_tools as tft
import tfb_strategy as tfsty
import tfb_backtest as tfbt


def main_bt(timStr='', nday=2):
    print('\nmain_bt,nday:', nday)
    tfsys.xnday_down = nday
    zsys.web_get001txtFg = True

    rs0 = './'
    fgid = rs0 + 'gid2017.dat'
    xtfb = tft.fb_init(rs0, fgid)
    if nday == -1:
        tfsys.xnday_down = xtfb.gid_nday + 10
        print('nday,', tfsys.xnday_down)

    print('\n#3,backtest')
    if nday != 0:
        xtfb.funPre = tfsty.sta00_pre
        xtfb.funSta = tfsty.sta01_sta
        xtfb.preVars = []
        xtfb.staVars = [1.25]

        #
        xtfb.kcid = '1'  # cn,3=bet365
        tfbt.bt_main(xtfb, timStr)

        #
        # 4---main_ret
        print('\n#4,result.anz')
        tfbt.bt_main_ret(xtfb, True)
        print('kcid,', xtfb.kcid, ',nday,', nday)
        print('preVar,', xtfb.preVars)
        print('staVar,', xtfb.staVars)
    #
    # 5
    tn = zt.timNSec('', xtfb.tim0, '')
    print('\n#5,backtest,tim:{0:.2f} s'.format(tn))
    #
    # 6---end.main
    print('\n#6,end.main')


timStr = ''
#
# 2#,get.data
# tfb_main.main_get('',2)
#
# 3#,backtest,main_bt
main_bt(timStr, 2)
