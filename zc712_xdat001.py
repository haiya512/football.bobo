# coding=utf-8
'''

'''

import arrow

import zsys
import ztools as zt
import ztools_web as zweb
import tfb_sys as tfsys
import tfb_tools as tft


def fb_gid_get_nday(xtfb, timeStr, fgExt=False):
    if not timeStr:
        ktim = xtfb.tim_now
    else:
        ktim = arrow.get(timeStr)

    # nday = tfsys.xnday_down
    nday = 2
    for tc in range(0, nday):
        xtim = ktim.shift(days=-tc)
        xtimStr = xtim.format('YYYY-MM-DD')
        # print('\nxtim',xtim,xtim<xtfb.tim0_gid)
        #
        xss = str(tc) + '#,' + xtimStr + ',@' + zt.get_fun_nam()
        zt.f_addLog(xss)
        if xtim < xtfb.tim0_gid:
            print('#brk;')
            break
        # 网页数据文件名
        fss = tfsys.rghtm + xtimStr + '.htm'
        uss = tfsys.us0_gid + xtimStr
        print(timeStr, tc, '#', fss)
        #
        htm = zweb.web_get001txtFg(uss, fss)
        if len(htm) > 5000:
            df = tft.fb_gid_get4htm(htm)
            if len(df['gid']) > 0:
                tfsys.gids = tfsys.gids.append(df)
                tfsys.gids.drop_duplicates(subset='gid', keep='last', inplace=True)
                #
                if fgExt:
                    tft.fb_gid_getExt(df)
                    # if fgExt:tft.fb_gid_getExtPool(df)
    # 如果设置保存数据文件名
    if tfsys.gidsFN:
        # print('')
        print(tfsys.gids.tail())
        tfsys.gids.to_csv(tfsys.gidsFN, index=False)


xtfb = tft.fb_init()
xtfb.gidsFN = 'tmp/gid01.csv'
zsys.web_get001txtFg = True
tim0 = arrow.get('2010-01-01')
tn = arrow.now() - tim0
tfsys.rghtm = tfsys.rxhtm = tfsys.rxdat = tfsys.rhtmOuzhi = 'tmp/'
timeStr = ''
nday = 2
# tfsys.xnday_down = nday
fb_gid_get_nday(xtfb, timeStr, fgExt=True)
