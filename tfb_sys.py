# -*- coding: utf-8 -*-
'''
'''
#

import arrow
import pandas as pd

gidNil = ['', '', '', '', '', '', '-1',
          '-1', '0', '0', '-1', '-1', '', '', '']
gidSgn = ['gid', 'gset', 'mplay', 'mtid', 'gplay', 'gtid', 'qj',
          'qs', 'qr', 'kend', 'kwin', 'kwinrq', 'tweek', 'tplay', 'tsell']
#
poolNil = ['', '', '', '', '', '', '-1', '-1', '0',
           '0', '-1', '-1', '', '', '', '0', 0, 0, 0, '-9']
poolSgn = ['gid', 'gset', 'mplay',
           'mtid', 'gplay', 'gtid', 'qj', 'qs', 'qr',
           'kend', 'kwin', 'kwinrq', 'tweek', 'tplay',
           'tsell', 'cid', 'pwin9', 'pdraw9', 'plost9', 'kwin_sta']
#

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
#retNil=[0,0,0,0, 0,0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0]
#retSgn=['kret9','kret3','kret1','kret0',  'knum9','knum3','knum1','knum0',  'ret9','num9','nwin9', 'ret3','num3','nwin3', 'ret1','num1','nwin1', 'ret0','num0','nwin0']

#--bt.var
btvarNil = ['', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '']
btvarSgn = ['xtim', 'kret9', 'kret3', 'kret1', 'kret0',
            'knum9', 'knum3', 'knum1', 'knum0', 'ret9', 'num9', 'nwin9',
            'ret3', 'ret1', 'ret0', 'nwin3', 'nwin1', 'nwin0',
            'num3', 'num1', 'num0',
            'v1', 'v2', 'v3', 'v4', 'v5', 'nday', 'doc']

# self.nsum,self.nwin,self.ndraw,self.nlost=0,0,0,0
# self.kwin,self.kdraw,self.klost=0,0,0
#-------------------
#
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
rmlib = rdat0 + 'mlib/'  # ai.mx.lib.xxx

# rgdat=rdat0+'gdat/'
#
rghtm = rdat0 + 'xhtm/ghtm/'  # gids_htm,days
rhtmOuzhi = rdat0 + 'xhtm/htm_oz/'
rhtmYazhi = rdat0 + 'xhtm/htm_az/'
rhtmShuju = rdat0 + 'xhtm/htm_sj/'
#

#---glibal.lib.xxx
gids = pd.DataFrame(columns=gidSgn, dtype=str)
xdats = pd.DataFrame(columns=gxdatSgn, dtype=str)

gidsFN = ''
gidsNum = len(gids.index)
xdatsNum = len(xdats.index)
#
xbars = None
xnday_down = 0


class zTopFoolball(object):
    '''
    设置TopFoolball项目的各个全局参数
    尽量做到all in one

    '''

    def __init__(self):
        self.tim0Str_gid = '2010-01-01'
        self.tim0_gid = arrow.get(self.tim0Str_gid)
        self.gid_tim0str = self.gid_tim9str = ''
        self.gid_nday = self.gid_nday_tim9 = 0
        self.tim0 = self.tim9 = self.tim_now = None
        self.tim0Str = self.tim9Str = self.timStr_now = ''
        #

        self.kgid = ''
        self.kcid = ''
        self.ktimStr = ''
        #
        self.poolInx = []
        self.poolDay = pd.DataFrame(columns=poolSgn)
        self.poolTrd = pd.DataFrame(columns=poolSgn)
        self.poolRet = pd.DataFrame(columns=retSgn)
        self.poolTrdFN = self.poolRetFN = ''
        #
        self.bars = None
        self.gid10 = None
        self.xdat10 = None

        self.funPre = self.funSta = None
        self.preVars = self.staVars = []
        self.ai_mxFN0 = ''
        self.ai_mx_sgn_lst = []
        self.ai_xlst = []
        self.ai_ysgn = ''
        self.ai_xdat = self.ai_xdat = None

        self.ret_nday = self.ret_nWin = 0
        self.ret_nplay = self.ret_nplayWin = 0

        self.ret_msum = 0


# ----------zTopFoolball.init.obj
