# -*- coding: utf-8 -*-
'''
'''

import numpy as np
import pandas as pd
import psutil as psu
from matplotlib import cm

__version__ = '2016.M10'

cpu_num_core = 8
cpu_num9 = 8
cpu_num = cpu_num9 - 1

tim0_sys = None
tim0_str = ''

fn_time_nloop = 5
fn_time_nloop5 = 500

file_dir = './'
gid_file_name = 'gid2017.dat'
gid_file = file_dir + gid_file_name

sgnSP4 = '    '
sgnSP8 = sgnSP4 + sgnSP4
# 日志文件名
logFN = ''
#
web_get001txtFg = False


# --colors
# 10,prism,brg,dark2,hsv,jet
# 10,,hot,Vega10,Vega20
cors_brg = cm.brg(np.linspace(0, 1, 10))
cors_hot = cm.hot(np.linspace(0, 1, 10))
cors_hsv = cm.hsv(np.linspace(0, 1, 10))
cors_jet = cm.jet(np.linspace(0, 1, 10))
cors_prism = cm.prism(np.linspace(0, 1, 10))
cors_Dark2 = cm.Dark2(np.linspace(0, 1, 10))
# cors_Vega10 = cm.Vega10(np.linspace(0, 1, 10))
# cors_Vega20 = cm.Vega20(np.linspace(0, 1, 10))


bs_get_ktag_kstr = ''
pd.set_option('display.width', 450)

if __name__ == "__main__":
    dn = psu.cpu_count(logical=False)
    print('main', dn)
