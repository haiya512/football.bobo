## 环境
* Python v3.5
* python v2.7
## 需要安装包
* arrow


>xdat2017.dat.utf8 太大，GitHub支持的单个文件大小上限为100M,
>推荐文件大小50M,所以都暂存在本地

### 目录层次
* xhtm 网页文件存档 默认包括四个子目录
* xhtm/ghtm 基本比赛数据网页文件 按日期保存
* xhtm/htm_oz  欧赔赔率网页文件,按gid比赛场次保存,每场比赛一个文件
* xhtm/htm_az  亚赔赔率网页文件
* xhtm/htm_sj  数据分析网页文件

### 数据文件gid2017字段意义
* gid 比赛场次ID编码，全局唯一(gameid)
* gset  game-set 联赛名称
* mplay main-play 主队
* mtid 主队编码ID
* gplaoy 客队
* gtid  客队编码ID
* qj 进球数
* qs 失球数
* qr 让球数
* kend  1代表比赛完结，0代码比赛取消
* kwin  比赛胜负情况, 3为主队胜，1为平局，0为客队胜，默认和取消的比赛为-1
* kwinrq 让球的比赛胜负情况 ，同上
* kwin_sta  ????
* tweek  比赛星期换算
* tplay 比赛日期
* tsell 博彩销售截止日期
*
* cid 菠菜公司ID  全局唯一
* cname 菠菜公司名称
* pwin0 pdraw0 plost0  开盘时主队胜平负的赔率
* vwin0 vdraw0 vlost0
* vwin0kaili vdraw0 vlost0  主队胜平负的 开盘凯利指数
* pwin9 pdraw9 plost9  收盘时主队胜平负的赔率
* vwin9 vdraw9 vlost9
* vwin9kaili vdraw9 vlost9  主队胜平负的 收盘凯利指数


### 数据文件列表
* gid2017.dat
* xdat2017.dat


### 脚本列表
##### 工具函数
* cpuinfo.py            cpu信息
* tfb_backtest.py       回测分析
* tfb_draw.py           画图脚本
* tfb_main.py           很多函数, 量化分析主程序入口
* tfb_strategy.py       常用策略函数
* tfb_sys.py            全局预定义变量,
* tfb_tools.py          工具函数

#### 计算脚本
* zc101_gid01des.py     获取排列前10名的比赛次数
* *zc401_dat_cut.py      文件切割, 示例用*
* zc402_dat_cutx.py     批量切割
* *zc404_gid_des.py      显示比赛总数前10名的球队，还有他们的球队比赛数占比, 示例用*
* zc405_gid_anz.py      计算各关键字段前10名的占比并画图
* zc406_gid_anz2.py     比赛场次年度数量的走势
* zc408_pv01.py         分析单个文件所有球队数据 *看不明白什么作用,获取4月份的数据?*
* zc409_pv02.py         生成各个参数的图片数据并保存
* zc501_pdx01.py        看的不是很懂,数学公式很多

* zc701.py              打开2010-01-01和今天的网页数据并保存为.html 很好奇,这个文件是以网站名字开头的,那么怎么合成gid和xdat呢?数据是不是合成这两个文件需要的呢?
* zc703_bs4_type.py     读取网页数据
* zc705_htmchk01.py
* zc706_gidget01.p
* zc709_gidall.py       保存近2天的数据
* zc712_xdat001.py      生成网页数据文件
* zc713_xdat002.py      从HTML文件获取某场比赛数据: 各大赔率等, 格式化并写入到tmp目录
* zc801_main_get.py     实盘数据更新
* zc802_xdat.py         看看读取文件花费的时间
* zc803_main_bt.py      一堆引用,MD
* zd401_sta01.py