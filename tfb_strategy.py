# -*- coding: utf-8 -*-
'''

'''
#
import ztop_ai as zai


def sta00_pre(xtfb):
    #
    return -9


def sta00_sta(xtfb, df):

    #
    return -9

#------------- sta01..sta


def sta01_sta(xtfb, df):
    xkwin, k0 = -9, xtfb.staVars[0]
    #---k0=1.1,k1=80
    df2 = df[df.cid == xtfb.kcid]
    if len(df2.index) > 0:
        dwin, dlose = df2['pwin0'][0], df2['plost0'][0]
        if dwin <= k0:
            xkwin = 3
        elif dlose <= k0:
            xkwin = 0
    #
    return xkwin


def sta01ext_sta(xtfb, df):
    xkwin, k30, k00 = -9, xtfb.staVars[0], xtfb.staVars[1]
    #---k0=1.1,k1=80
    df2 = df[df.cid == xtfb.kcid]
    if len(df2.index) > 0:
        dwin, dlose = df2['pwin0'][0], df2['plost0'][0]
        if dwin <= k30:
            xkwin = 3
        elif dlose <= k00:
            xkwin = 0
    #
    return xkwin


def sta10_sta(xtfb, df):
    xkwin, k0, k1 = -9, xtfb.staVars[0], xtfb.staVars[1]
    #---k0=1.1,k1=80
    df3 = df[df.pwin0 < k0]
    df0 = df[df.plost0 < k0]
    xn9 = len(df.index)
    if xn9 > 0:
        kn3, kn0 = len(df3.index) / xn9 * 100, len(df0.index) / xn9 * 100
        if kn3 > k1:
            xkwin = 3
        elif kn0 > k1:
            xkwin = 0
    #
    return xkwin

#------------- sta30.mul.sta


def sta310_pre(xtfb):
    df = xtfb.xdat10
    #
    df['kpwin'] = round(df['pwin9'] / df['pwin0'] * 100)
    df['kplost'] = round(df['plost9'] / df['plost0'] * 100)
    df['kpdraw'] = round(df['pdraw9'] / df['pdraw0'] * 100)
    #
    return df


def sta310_sta3(xtfb, df):
    df9 = df[df.kpwin > 100]
    df1 = df[df.kpwin <= 100]
    xn = len(df1.index) - len(df9.index)
    #
    xkwin, k0 = -9, xtfb.staVars[0]
    if xn > k0:
        xkwin = 3
    #
    return xkwin


def sta310_sta1(xtfb, df):
    df9 = df[df.kpdraw > 100]
    df1 = df[df.kpdraw <= 100]
    xn = len(df1.index) - len(df9.index)
    #
    xkwin, k0 = -9, xtfb.staVars[0]
    if xn > k0:
        xkwin = 1
    #
    return xkwin


def sta310_sta0(xtfb, df):
    df9 = df[df.kplost > 100]
    df1 = df[df.kplost <= 100]
    xn = len(df1.index) - len(df9.index)
    #
    xkwin, k0 = -9, xtfb.staVars[0]
    if xn > k0:
        xkwin = 0
    #
    return xkwin


def sta310_sta(xtfb, df):
    xkwin = -9
    xk3, xk1, xk0 = sta310_sta3(xtfb, df), sta310_sta1(
        xtfb, df), sta310_sta0(xtfb, df)
    if (xk3 == 3)and(xk1 < 0)and(xk0 < 1):
        xkwin = 3
    if (xk3 < 1)and(xk1 == 1)and(xk0 < 0):
        xkwin = 1
    if (xk3 < 1)and(xk1 < 0)and(xk0 == 0):
        xkwin = 0
    #
    # print('sta',xkwin,xk3,xk1,xk0)
    return xkwin


#------------- sta.ai.xxx


def sta_ai_log01(xtfb, df):
    # 1
    xkwin, k00, k10, k30 = - \
        9, xtfb.staVars[0], xtfb.staVars[1], xtfb.staVars[2]
    ysgn = 'kwin'  # xtfb.ai_ysgn
    # 2
    df[ysgn] = df[ysgn].astype(str)
    df[ysgn].replace('3', '2', inplace=True)
    # 3
    df[ysgn] = df[ysgn].astype(int)
    # 4
    xtfb.ai_xdat, xtfb.ai_ydat = df[xtfb.ai_xlst], df[ysgn]
    # 5
    msgn = xtfb.ai_mx_sgn_lst[0]  # 'log'
    mx = zai.xmodel[msgn]
    dacc, df9 = zai.mx_fun8mx(
        mx, xtfb.ai_xdat, xtfb.ai_ydat, yk0=1, fgInt=True)  # ,fgDebug=True
    # 6
    df3, df1, df0 = df9[df9['y_pred'] == 2], df9[
        df9['y_pred'] == 1], df9[df9['y_pred'] == 0]
    dn3, dn1, dn0 = len(df3.index), len(df1.index), len(df0.index)
    # 7
    dn9, dsum = max(dn3, dn1, dn0), sum([dn3, dn1, dn0])
    # 8
    if dsum > 0:
        dk3, dk1, dk0 = dn3 / dsum * 100, dn1 / dsum * 100, dn0 / dsum * 100
        if (dn3 == dn9)and(dk3 > k30):
            xkwin = 3
        elif (dn1 == dn9)and(dk1 > k10):
            xkwin = 1
        elif (dn0 == dn9)and(dk0 > k00):
            xkwin = 0
        #
        # yk310=df9['y_test'][0]
        # xs0='@log01,{0}#,{1},xk,gid,{2},dsum.{3},dn310,{4},{5},{6},dk310,{7:.1f}%,{8:.1f}%,{9:.1f}%'
        # xss=xs0.format(xkwin,yk310,xtfb.kgid,dsum,dn3,dn1,dn0,dk3,dk1,dk0)
        # print(xss)

    # 9
    return xkwin
