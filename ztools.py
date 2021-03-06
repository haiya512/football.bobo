# coding:utf-8
'''
文件名:ztools.py
默认缩写：import ztools as zt
简介：Top极宽常用工具函数集
'''

import os
import sys
import random
import inspect
import pickle
import time

import arrow
import numexpr as ne

import pandas as pd

import psutil as psu

import matplotlib as mpl

import cpuinfo as cpu
import zsys
import ztools_str as zstr


def initSysVar(fgView=False):
    '''
    初始化系统环境参数，以及部分全局变量
    '''
    mpl.style.use('seaborn-whitegrid')
    pd.set_option('display.width', 450)
    #
    zsys.tim0_sys = arrow.now()
    zsys.tim0_str = zsys.tim0_sys.format('YYYY-MM-DD HH:mm:ss')

    zsys.cpu_num_core = psu.cpu_count(logical=False)
    zsys.cpu_num9 = psu.cpu_count()
    zsys.cpu_num = round(zsys.cpu_num9 * 0.8)
    ne.set_num_threads(zsys.cpu_num)
    #
    if fgView:
        print('cpu_num_core:', zsys.cpu_num_core)
        print('cpu_num9:', zsys.cpu_num9)
        print('cpu_num:', zsys.cpu_num)
        #
        print('tim0_str:', zsys.tim0_str)
        print('tim0_sys:', zsys.tim0_sys)
        #
        print('tim0.year:', zsys.tim0_sys.year)
        print('tim0.month:', zsys.tim0_sys.month)
        print('tim0.day:', zsys.tim0_sys.day)
        #
        print('tim0.shift(-2):', zsys.tim0_sys.shift(days=-2))
        print('tim0.shift(2):', zsys.tim0_sys.shift(days=2))


def get_fun_nam():
    # 解析堆栈, 感觉没啥用
    # 如果是在centos下面跑,会有问题, 不知道Python3是不是这样
    return inspect.stack()[1][3]


def xinEQ(d, k0, k9):
    ''' 如果d位于(k0, k9)间，包含等于，返回True
                    d可以是数值，字符串
    '''
    # return (d>=k0)&(d<=k9)
    return ne.evaluate('(d>=k0)&(d<=k9)')


def xin(xk, k0sgn, k9sgn):
    ''' 如果xk位于(x0sgn, x9sgn)间，不含等于，返回True
       xk可以是数值，字符串
    '''

    # return (xk>k0sgn)&(xk<k9sgn)
    return ne.evaluate('(xk>k0sgn)&(xk<k9sgn)')


def iff2(kflag, x1, x0):
    ''' 二选一函数，如果kflag为True，返回值是x1；否则，返回值是x0；
        Args:
        kflag (bool): true or fall
        '''

    if kflag:
        return x1
    else:
        return x0


def iff3(v, k, xn1, x0, x1):
    ''' 三选一函数，如果v<k，返回值是xn1；v=k，返回值是x0；v>k，返回值是x1；
    '''

    if v < k:
        return xn1
    elif v == k:
        return x0
    else:
        return x1


def wait(n, mstr=''):
    ''' 等待n秒，mstr为提示信息
    '''

    if mstr != '':
        print(mstr)

    time.sleep(n)


    # def cpu_chk():
    try:
        cpu._check_arch()
    except Exception as err:
        sys.stderr.write(str(err) + "\n")
        sys.exit(1)

    info = cpu.get_cpu_info()
    if info:
        print('cpu 型号: {0}'.format(info.get('brand', '')))
        print('最高主频 Hz: {0}'.format(info.get('hz_advertised', '')))
        print('实际主频 Hz: {0}'.format(info.get('hz_actual', '')))


def xobj2str(xobj, xnamLst):
    ''' 对象属性字符串，根据属性列表，生成字符串

        #qxLibName=['time','ID','stkVal','cash','dret','val'];
        '''

    # print('\n::QxUsr');
    dss = ''
    for cnam in xnamLst:
        ess = str(xobj[cnam])
        dss = dss + cnam + ',' + ess + '; '

    return dss


def xobjPr(rx):
    t5 = []
    for xnam, xdat in vars(rx).items():
        dss = '{0:15} = '.format(xnam)
        dat = '{0}'.format(xdat)
        if len(dat) > 50:
            dat = '......'
        dss = ''.join([dss, dat])
        t5.append(dss)
    # sorted(t5)
    t5.sort()
    lstPr(t5)


def lst4objs_txt(xobjs, fltLst=[]):
    clst = []
    for x in xobjs:
        # css=x.text.replace('\n','')
        css = zstr.str_flt(x.get_text(), fltLst)
        c20 = css.split(' ')
        for c in c20:
            if c != '':
                clst.append(c)
    #
    return clst


def lst4dir(rss):
    ''' 目录文件生成列表数据
    '''

    flst = []
    for root, dirs, files in os.walk(rss):
        for fss in files:
            # print(fss)
            flst.append(fss)
    return flst


def lstPr(lst):
    ''' 输出列表信息
    '''

    for x in lst:
        print(x)


def lst_keyGetStr(dlst, kstr0):
    xlst = []
    kstr = kstr0.upper()
    ksn = len(kstr0)
    for xd in dlst:
        x = str(xd)
        print(len(x), '#', kstr, x)
        if len(x) > ksn:
            print(kstr, x)
            if x.upper().find(kstr) > -1:
                xlst.append(x)  # print(kstr,x)
    #
    return xlst


def lst_keyFltStr(dlst, kstr0):
    xlst, kstr, ksn = [], kstr0.upper(), len(kstr0)
    for xd in dlst:
        x = str(xd)
        if len(x) > ksn:
            if x.upper().find(kstr) == -1:
                xlst.append(x)
    #
    return xlst


def f_addLog(dss):
    # 如果设置了日志文件名
    if zsys.logFN:
        timStr = arrow.now().format('YYYY:MM:DD HH:mm:ss')
        tss = timStr + '-->  ' + dss  # print('log,',tss)
        f_add(zsys.logFN, tss)


def f_size(filename):
    if os.path.exists(filename):
        return os.path.getsize(filename)
    else:
        return 0


def f_rd(fn):
    with open(fn, 'r') as f:
        content = f.read()
    return content


def f_rdXHdr(fn, cod='gbk'):
    with open(fn, 'r', encoding=cod) as f:
        hdr = f.readline()
        dss = f.read()
    return hdr, dss


def f_rdXNum(fn, cod='gbk'):
    with open(fn, 'r', encoding=cod) as f:
        dss = f.readline()
    dn = int(dss)
    return dn


def f_add(filename, content):
    """
    内容写入文件的函数
    :param filename:
    :param content:
    :return:
    """
    if os.path.isfile(filename):
        f = open(filename, 'w')
    else:
        f = open(filename, 'a')
    f.write(content + '\n')
    f.close()


def f_addLst(fn, xlst, fgNew=True, cod='utf-8'):
    if fgNew:
        f = open(fn, 'w', encoding=cod)
    else:
        f = open(fn, 'a', encoding=cod)
    tss = ''
    for x in xlst:
        tss = tss + str(x) + '\n'
    f.write(tss + '\n')
    f.close()


def f_getSize(fn):
    fsize = 0
    if os.path.exists(fn):
        fsize = os.path.getsize(fn)
    return fsize


def f_lstRndN(xlst, xn):
    '''
    @call.demo:
    x10=zt.lstRndN(xlst,80);ds=pd.Series(x10);ds.name='code'
    ds.to_csv('tmp\cod080.csv',index=False,header='code')
    '''
    x10 = set()
    xn9 = len(xlst)
    while len(x10) < xn:
        xc = random.randint(0, xn9)
        # print(xc,x10,'n',len(x10),xn9)
        x1 = xlst[xc]
        x10.add(x1)

    return list(x10)


def f_lstRd(fnam):
    ''' 读取列表数据
    '''

    with open(fnam, 'rb') as f:
        lst = pickle.load(f)
    return lst


def f_lstWr(fnam, lst):
    ''' 保存列表数据
    '''

    fhnd = open(fnam, 'wb')
    pickle.dump(lst, fhnd)  # ,True
    fhnd.close()


def f_lstWrTxt(fnam, lst):
    f = open(fnam, 'w')
    for x in lst:
        f.write(x)
        f.write("\n")
    #
    f.close()


def f_lstRdTxt(fnam):
    f = open(fnam, 'r')
    lines = f.readlines()
    f.close()
    #
    xlst = []
    for tmp in lines:
        tmp = tmp.replace('\n', '')
        tmp = tmp.replace('"', '').split(',')

        # del(temp[0])
        # del(tmp[:-1])
        xlst.append(tmp)
    #
    return xlst


def tim_now_str():
    dss = arrow.now().format('YYYY-MM-DD HH:mm:ss')
    return dss


def timNSec(tim, tim0, fgPr=False):
    # 获取时间差
    if not tim:
        tim = arrow.now()
    if isinstance(tim, str):
        tim = arrow.get(tim)
    tn = tim - tim0
    xn = round(tn.total_seconds(), 2)
    if fgPr:
        print(xn, 's,', tim.format('HH:mm:ss'),
              ',t0,', tim0.format('HH:mm:ss'))
    return xn


def timNHour(tim, tim0, fgPr=False):
    if tim == '':
        tim = arrow.now()
    if type(tim) == str:
        tim = arrow.get(tim)
    tn = tim - tim0
    xn = round(tn.total_seconds(), 2)
    hn = round(xn / 3600, 2)
    if fgPr:
        print(hn, ' hours,', tim.format('HH:mm:ss'),
              ',t0,', tim0.format('HH:mm:ss'))
    return hn


def timNDay(time, tim0, fgPr=False):
    '''
    返回一个天数
    :param tim:
    :param tim0:
    :param fgPr:
    :return:
    '''
    if not time:
        time = arrow.now()
    if isinstance(time, str):
        time = arrow.get(time)
    # 求得间隔秒数
    tn = time - tim0
    xn = round(tn.total_seconds(), 2)
    day_nums = round(xn / 3600 / 24)
    if fgPr:
        print(day_nums, ' days,', time.format('YYYY-MM-DD'),
              ',t0,', tim0.format('YYYY-MM-DD'))
    return day_nums


def maxium_fun(sp_dict):
    '''
    接收一个长度为3的字典,字典的3个键为3,1,0,分别代表胜平负
    value为开出的对应的SP,因为开出的赔率值有可能相同(虽然少,还是有可能的),
    所以返回的结果应该是key组成的list
    返回的是从赔率的最小值判断出的结果
    :param sp_dict:
    :return:
    '''
    if not isinstance(sp_dict, dict) or len(sp_dict) != 3:
        print("ERROR: not a dict or dict length is not 3")
        return False
    value_list = [str(sp_dict[key]) for key in sp_dict]
    min_sp = min(value_list)
    min_sp_result = [str(key) for key in sp_dict if sp_dict[key] == min_sp]
    return min_sp_result


def score_kwin_result(mplay_score, gplay_score, rq=0):
    """
    传递主场得分和客场得分,然后得到比赛结果
    :param mplay_score:
    :param gplay_score:
    :return:
    """

    mplay_score = int(mplay_score)
    gplay_score = int(gplay_score)
    # print(mplay_score,gplay_score,rq)
    if rq:
        mplay_score = mplay_score + int(rq)
    if mplay_score > gplay_score:
        result = '3'
    if mplay_score == gplay_score:
        result = '1'
    if mplay_score < gplay_score:
        result = '0'
    return result
