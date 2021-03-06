# -*- coding: utf-8 -*-
'''
'''

import arrow
import pandas as pd

# df的初始默认值
gidNil = [
    '', '', '', '',
    # '-1', '-1', '0',
    '0',
    #
    '2', '-1', '-1',
    # '', '', ''
    '', '',
    '', '',
]
# df 的列名
gidSgn = [
    # 'gid', 'gset', 'mplay', 'mtid', 'gplay', 'gtid',
    'gid', 'gset', 'mplay', 'gplay',
    # 'qj', 'qs', 'qr',
    'qr',
    'kend', 'kwin', 'kwinrq',
    # 'tweek', 'tplay', 'tsell',
    'nml_sp_result', 'rp_sp_result',
    'tplay', 'tsell',
]

poolNil = ['', '', '', '', '', '', '-1', '-1', '0',
           '0', '-1', '-1', '', '', '', '0', 0, 0, 0, '-9']
poolSgn = ['gid', 'gset',
           'mplay', 'mtid', 'gplay', 'gtid',
           'qj', 'qs', 'qr',
           'kend', 'kwin', 'kwinrq',
           'tweek', 'tplay', 'tsell',
           'cid', 'pwin9', 'pdraw9', 'plost9', 'kwin_sta']

gxdatNil = ['', '', '', 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            '', '', '', '', '', '-1', '-1', '0', '-1', '-1', '', '']
gxdatSgn = ['gid', 'cid', 'cname',
            'pwin0', 'pdraw0', 'plost0', 'pwin9', 'pdraw9', 'plost9',
            'vwin0', 'vdraw0', 'vlost0', 'vwin9', 'vdraw9', 'vlost9',
            'vback0', 'vback9',
            'vwin0kali', 'vdraw0kali', 'vlost0kali',
            'vwin9kali', 'vdraw9kali', 'vlost9kali',
            'gset', 'mplay', 'mtid', 'gplay', 'gtid',
            'qj', 'qs', 'qr', 'kwin', 'kwinrq',
            'tweek', 'tplay']
#
retNil = ['', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
retSgn = ['xtim', 'kret9', 'kret3', 'kret1', 'kret0',
          'knum9', 'knum3', 'knum1', 'knum0', 'ret9',
          'num9', 'nwin9', 'ret3', 'ret1', 'ret0',
          'nwin3', 'nwin1', 'nwin0', 'num3', 'num1', 'num0']
# retNil=[0,0,0,0, 0,0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0]
# retSgn=['kret9','kret3','kret1','kret0',  'knum9','knum3','knum1','knum0',  'ret9','num9','nwin9', 'ret3','num3','nwin3', 'ret1','num1','nwin1', 'ret0','num0','nwin0']

btvarNil = ['', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '']
btvarSgn = ['xtim', 'kret9', 'kret3', 'kret1', 'kret0',
            'knum9', 'knum3', 'knum1', 'knum0', 'ret9', 'num9', 'nwin9',
            'ret3', 'ret1', 'ret0', 'nwin3', 'nwin1', 'nwin0',
            'num3', 'num1', 'num0',
            'v1', 'v2', 'v3', 'v4', 'v5', 'nday', 'doc']


# us0='http://trade.500.com/jczq/?date='
# http://odds.500.com/fenxi/shuju-278181.shtml
# http://odds.500.com/fenxi/yazhi-278181.shtml
# http://odds.500.com/fenxi/ouzhi-278181.shtml
us0_gid = 'http://trade.500.com/jczq/?date='
us0_ext0 = 'http://odds.500.com/fenxi/'
us0_extOuzhi = us0_ext0 + 'ouzhi-'
us0_extYazhi = us0_ext0 + 'yazhi-'
us0_extShuju = us0_ext0 + 'shuju-'
#
rdat0 = './'
# rdat0 = '/tfbDat/'
rxdat = rdat0 + 'xdat/'
rmdat = rdat0 + 'mdat/'
rmlib = rdat0 + 'mlib/'

# rgdat=rdat0+'gdat/'
#
rghtm = rdat0 + 'xhtm/ghtm/'
rhtmOuzhi = rdat0 + 'xhtm/htm_oz/'
rhtmYazhi = rdat0 + 'xhtm/htm_az/'
rhtmShuju = rdat0 + 'xhtm/htm_sj/'
#

# ---glibal.lib.xxx
gids = pd.DataFrame(columns=gidSgn, dtype=str)
xdats = pd.DataFrame(columns=gxdatSgn, dtype=str)

# gid file name, gid文件名称
gidsFN = ''
gidsNum = len(gids.index)
xdatsNum = len(xdats.index)
#
xbars = None
# 数据下载的天数(偏离今天的时间长度)
xnday_down = 0


class zTopFoolball(object):
    '''
    设置TopFoolball项目的各个全局参数
    尽量做到all in one
    '''

    def __init__(self):
        self.tim0Str_gid = '2010-01-01'
        self.tim0_gid = arrow.get(self.tim0Str_gid)

        self.gid_tim0str = ''
        self.gid_tim9str = ''

        self.gid_nday = 0
        self.gid_nday_tim9 = 0

        self.tim0 = None
        self.tim9 = None
        self.tim_now = None

        self.tim0Str = ''
        self.tim9Str = ''
        self.timStr_now = ''

        self.kgid = ''
        self.kcid = ''
        self.ktimStr = ''

        # 比赛索引数据, 只有gid编码和一天的数据
        self.poolInx = []
        # 各场比赛的赔率数据, 只有一天的数据
        self.poolDay = pd.DataFrame(columns=poolSgn)
        # 总的交易数据, 包括多日的数据, 是gid数据的增强版本
        self.poolTrd = pd.DataFrame(columns=poolSgn)
        # 每天的回报率记录,包括多日的数据
        self.poolRet = pd.DataFrame(columns=retSgn)

        self.poolTrdFN = ''
        self.poolRetFN = ''

        self.bars = None

        self.gid10 = None
        self.xdat10 = None

        # 策略函数返回的推荐结果或者策略函数
        self.funPre = None
        self.funSta = None

        self.preVars = self.staVars = []

        self.ai_mxFN0 = ''
        self.ai_mx_sgn_lst = []
        self.ai_xlst = []
        self.ai_ysgn = ''
        self.ai_xdat = None
        self.ai_xdat = None

        self.ret_nday = 0
        self.ret_nWin = 0
        self.ret_nplay = 0
        self.ret_nplayWin = 0
        self.ret_msum = 0
