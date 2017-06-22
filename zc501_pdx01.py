# coding=utf-8

import pandas as pd

rs0 = './'
# fdat=rs0+'xdat2017.dat'
fdat = 'dat/xd_2016.dat'
df = pd.read_csv(fdat, index_col=False, dtype=str)
gid = '512751'
dfk = df[df['gid'] == gid]
df2 = dfk[dfk['cid'] < '90000']


print(df2.describe())
print(df2.tail())

print(dfk.tail())
#
ds = pd.Series()
ksgn = 'pwin0'
df2[ksgn] = df2[ksgn].astype(float)
ds['xmin'] = df2[ksgn].min()
ds['xmax'] = df2[ksgn].max()

ds['xavg'] = df2[ksgn].mean()
ds['xmed'] = df2[ksgn].median()
#
ds['q-0.1'] = df2[ksgn].quantile(0.1)
ds['q-0.25'] = df2[ksgn].quantile(0.25)
ds['q-0.5'] = df2[ksgn].quantile(0.5)
ds['q-0.75'] = df2[ksgn].quantile(0.75)
ds['q-0.9'] = df2[ksgn].quantile(0.9)
#
ds['xmad'] = df2[ksgn].mad()
ds['var'] = df2[ksgn].var()
ds['std'] = df2[ksgn].std()
ds['skew'] = df2[ksgn].skew()
ds['kurt'] = df2[ksgn].kurt()
#
ds['cumsum'] = df2[ksgn].cumsum()
ds['cummin'] = df2[ksgn].cummin()
ds['cumprod'] = df2[ksgn].cumprod()
#
ds['diff'] = df2[ksgn].diff()
ds['pct_change'] = df2[ksgn].pct_change()

print('\n#4')
print(ds)

print('\nok,!')
'''
	count	，计算非 NA 值的数量。
	describe，针对 Series 或 DF 的列计算汇总统计。
	min , max，最小值和最大值。
	argmin , argmax，最小值和最大值的索引位置（整数）。
	idxmin , idxmax，最小值和最大值的索引值。
	quantile，样本分位数（0 到 1）。
	sum，求和。
	mean，均值。
	median，中位数。
	mad，根据均值计算平均绝对离差。
	var，方差。
	std，标准差。
	skew，样本值的偏度（三阶矩）。
	kurt，样本值的峰度（四阶矩）。
	cumsum，样本值的累计和。
	cummin , cummax，样本值的累计最大值和累计最小值。
	cumprod，样本值的累计积。
	diff，计算一阶差分（对时间序列很有用）。
	pct_change，计算百分数变化。

print(dfk.tail())

dfk['inx']=dfk['tplay']
dfk.reindex(['inx'])

print('\n#2')
print(dfk.tail())
dfk=dfk.sortindex()

print('\n#3')
print(dfk.tail())

gid   gset  mplay   mtid  gplay   gtid     qj     qs     qr   kend   kwin kwinrq  tweek       tplay                tsell
count    68522  68521  68521  68517  68521  68517  68522  68522  68522  68522  68522  68522  68522       68522                68522
unique   68522    154   2007   1724   1958   1681     14     11      1      2      4      1      7        2530                14785
top     438989     英甲    布里斯    653    布里斯    653      1      1      0      1      3     -1      6  2016-05-08  2013-02-08 23:30:00
freq         1   3807    277    218    280    220  22219  23830  68522  68365  30810  68522  22940         103                  131
'''
