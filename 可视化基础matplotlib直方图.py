##折线图、散点图plot
import matplotlib.pylab as pyl
import numpy as npy
import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np
import matplotlib


##my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\STSONG.TTF")
font = {'family':'MicroSoft YaHei',
        'weight':'bold',
        'size':'larger'}
matplotlib.rc('font',**font)

pyl.subplot(3,1,1)#定位图片显示位置(行，列，当前区域位置)
x=[1,2,3,4,8]
y=[5,7,2,1,5]

##pyl.plot(x,y,'oy')#plot(x轴数据，y轴数据，展现形式) 默认折线图，o是散点图
pyl.plot(x,y,'c-.')
##plt.plot(横,纵,linestyle=':',color='b',linewidth=5,marker='.')
##plt.bar([数字设置横轴刻度位 非名字],color='blue',alpha=0.7,data)
##plt.grid(color,linestyle,axis='y')#默认y轴
##plt.bar(横轴,值,bottom=data1,label='')#堆积图，设置最下方数据源
##plt.bar(横轴,值+3,data2,width=3,label='')#横排并列，设置条形宽度，label设置图例
##plt.barh()#横向直方图
###linestyle:-,-.,.,--  color:r,g,w,b   marker突出线上的点   alpha透明度  grid网格


'''
c-cyan-青色  r-red  m-magente-品红  g-green  b-blue  y-yellow  k-black  w-white
'''

##线条样式
'''
- 直线  --  虚线  -.  就是-.  :   细小虚线  '''

#点的样式
'''
s--方形  h--六角形  H--六角形  *--星形+--加号  x--x型  d--菱形  D--菱形  p--五角形
'''

pyl.subplot(3,2,3)
x2=[1,3,6,8,10,12,19]
y2=[1,6,9,10,19,23,35]
pyl.plot(x2,y2,'y--')#x/y必须同样个数

pyl.title('show')
pyl.xlabel('ages')
pyl.ylabel('temp')
pyl.xlim(0,20)#横轴范围
pyl.ylim(0,40)#纵轴范围
plt.xticks(range(2,26,2))#设置横轴的刻度位置

#随机数的生成
pyl.subplot(3,2,4)#定位图片显示位置(行，列，当前区域位置)
data1 = np.random.normal(10.0,1.0,1000)#(均数,sigma，个数)
pyl.hist(data1)


#分布直方图hist(x轴参数范围，y轴参数个数)
pyl.subplot(3,1,3)
data2 = np.random.randint(1,25,1000)#(最小值，最大值，个数)
sty = np.arange(2,19,4)#设置直方图宽即x轴(最小值，最大值，步长)
pyl.hist(data2,sty)#绘制直方图，sty为直方图格式如上

#温度分布10-12点
x3=range(0,120)
y3=[np.random.randint(20,35) for i in range(120)]
plt.figure(figsize=(10,6),dpi=80)#设置格式大小，清晰度
plt.plot(x3,y3)

_x = list(x3)[::10]#修改步长
_xtick_labels = ["10点{}分".format(i) for i in range(60)]
_xtick_labels += ["11点{}分".format(i) for i in range(60)]
plt.xticks(_x3,_xtick_labels[::10],rotation=45,fontproperties=my_font)#修改横轴名字,把横轴坐标竖过来
##plt.savefig('./t1.png')保存图片


pyl.show()















