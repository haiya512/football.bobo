# coding=utf-8
'''
实盘数据更新
'''


import zsys
import ztools as zt

#
import tfb_sys as tfsys
import tfb_tools as tft


def main_get(timStr='', nday=2):
    #
    # 1---init.sys
    print('\nmain_get,nday:', nday)
    tfsys.xnday_down = nday
    zsys.web_get001txtFg = True

    #
    # 2---init.tfb
    rs0 = './'
    fgid = rs0 + 'gid2017.dat'
    xtfb = tft.fb_init(rs0, fgid)
    if nday == -1:
        tfsys.xnday_down = xtfb.gid_nday + 10
        print('nday,', tfsys.xnday_down)

    #
    # 3---update.data
    print('\n#3,update.data')
    if nday != 0:
        tft.fb_gid_get_nday(xtfb, timStr, fgExt=True)
    #
    # 4
    tn = zt.timNSec(timStr, xtfb.tim0, '')
    print('\n#4,update.data,tim:{0:.2f} s'.format(tn))
    #


main_get('', 2)
print('\nok!')
