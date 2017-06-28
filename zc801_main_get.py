# coding=utf-8
'''
实盘数据更新
'''

import zsys
import ztools as zt

import tfb_sys as tfsys
import tfb_tools as tft
from zsys import gid_file, file_dir


def main_get(timeStr='', nday=2):
    tfsys.xnday_down = nday
    # 是否重新获取网页数据
    # zsys.web_get001txtFg = True
    zsys.web_get001txtFg = False

    # rs0 = './'
    # xtfb = tft.fb_init(rs0, gid_file)
    xtfb = tft.fb_init(file_dir, gid_file)
    if nday == -1:
        tfsys.xnday_down = xtfb.gid_nday + 10
        print('nday,', tfsys.xnday_down)

    if nday != 0:
        tft.fb_gid_get_nday(xtfb, timeStr, nday=nday, fgExt=True)

    # 获取时间差
    tn = zt.timNSec(timeStr, xtfb.tim0, '')


main_get()
