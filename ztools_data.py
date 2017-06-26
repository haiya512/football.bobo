# coding: utf-8

import pandas as pd


def fb_df_type2float(df, xlst):
    for xsgn in xlst:
        df[xsgn] = df[xsgn].astype(float)


def fb_df_type4mlst(df, nlst, flst):
    for xsgn in nlst:
        df[xsgn] = df[xsgn].astype(int)

    for xsgn in flst:
        df[xsgn] = df[xsgn].astype(float)


def df_type2float(df, xlst):
    for xsgn in xlst:
        df[xsgn] = df[xsgn].astype(float)


def df_type4mlst(df, nlst, flst):
    for xsgn in nlst:
        df[xsgn] = df[xsgn].astype(int)

    for xsgn in flst:
        df[xsgn] = df[xsgn].astype(float)


def df_2ds8xlst(df, ds, xlst):
    for xss in xlst:
        ds[xss] = df[xss]

    # df9.to_csv(ftg,index=False,encoding='gbk')
    return ds


def df_get8tim(df, ksgn, kpre, kn9, kpos):
    #
    xdf = pd.DataFrame(columns=['nam', 'dnum'])
    ds = pd.Series(['', 0], index=['nam', 'dnum'])
    for xc in range(1, kn9 + 1):
        xss, kss = '{0:02d}'.format(xc), '{0}{1:02d}'.format(kpre, xc)
        df2 = df[df[ksgn].str.find(kss) == kpos]
        ds['nam'], ds['dnum'] = xss, len(df2['gid'])
        xdf = xdf.append(ds.T, ignore_index=True)
        # print(xc,'#',xss,kss)
    #
    xdf.index = xdf['nam']
    return xdf


def df_kcut8tim(df, ksgn, tim0str, tim9str):
    """
    df pandas.dataframe
    :param df: pandas data
    :param ksgn:  key world columns
    :param tim0str: start time
    :param tim9str:  stop time
    :return: df
    """
    df2 = df[tim0str <= df[ksgn]]
    df3 = df2[df2[ksgn] <= tim9str]
    return df3


def df_kcut8yearlst(df, ksgn, ftg0, yearlst):
    """
    给一个年份列表: 元素格式如: 2010-01-01, 按照每年来切割成为一个文件
    :param df:
    :param ksgn:
    :param ftg0:  file path or dir path
    :param yearlst:
    :return:
    """
    for ystr in yearlst:
        tim0str = ystr + '-01-01'
        tim9str = ystr + '-12-31'
        df2 = df_kcut8tim(df, ksgn, tim0str, tim9str)
        ftg = ftg0 + ystr + '.dat'
        df2.to_csv(ftg, index=False)


def df_kcut8myearlst(df, ksgn, tim0str, ftg0, yearlst):
    """
    给一个年份列表, 累计的来切割查看走势
    :param df:
    :param ksgn:
    :param tim0str:
    :param ftg0:
    :param yearlst:
    :return:
    """
    for ystr in yearlst:
        tim9str = ystr + '-12-31'
        df2 = df_kcut8tim(df, ksgn, tim0str, tim9str)
        ftg = ftg0 + ystr + '.dat'
        print(ftg)
        df2.to_csv(ftg, index=False)
