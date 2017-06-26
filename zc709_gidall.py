# coding: utf-8
'''

'''
import arrow
import zsys
import ztools as zt
import ztools_web as zweb
import tfb_sys as tfsys
# import tfb_tools as tft
from tfb_tools import fb_init, fb_gid_get4htm, fb_gid_getExt
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


def fb_gid_get_nday(xtfb, timeStr, fgExt=False, nday=0):
    if not timeStr:
        ktime = xtfb.tim_now
    else:
        ktime = arrow.get(timeStr)

    if not nday:
        print("nday should not be 0")
        return False
    for tc in range(0, nday):
        xtime = ktime.shift(days=-tc)
        # print("xtim: ", xtim)
        xtimeStr = xtime.format('YYYY-MM-DD')
        # print('\nxtim',xtim,xtim<xtfb.tim0_gid)
        # 这个是日志文件内容
        log_content = str(tc) + '#,' + xtimeStr + ',@' + zt.get_fun_nam()
        zt.f_addLog(log_content)
        if xtime < xtfb.tim0_gid:
            # 如果当前的时间早于2010-01-01
            # print('#brk;')
            break

        html_filename = tfsys.rghtm + xtimeStr + '.htm'
        url = tfsys.us0_gid + xtimeStr
        print url
        htm = zweb.web_get001txtFg(url, html_filename)
        if len(htm) > 5000:
            df = fb_gid_get4htm(htm)
            # 如果有比赛
            if len(df['gid']) > 0:
                tfsys.gids = tfsys.gids.append(df)
                # 去除重复行函数
                tfsys.gids.drop_duplicates(subset='gid', keep='last', inplace=True)
                #
                if fgExt:
                    fb_gid_getExt(df)
                # if fgExt:tft.fb_gid_getExtPool(df)
    # 如果设置了xx文件名,就写入到文件
    if tfsys.gidsFN:
        # print(tfsys.gids.tail())
        tfsys.gids.to_csv(tfsys.gidsFN, index=False)



xtfb = fb_init()
tfsys.gidsFN = 'tmp/gid01.csv'
zsys.web_get001txtFg = True

# tn = arrow.now() - arrow.get('2010-01-01')
# print('tn,',tn)

timeStr = ''
# 算最近两天的数值
fb_gid_get_nday(xtfb, timeStr, fgExt=False, nday=2)

# df=zfbt.fb_gidGet(hss)
