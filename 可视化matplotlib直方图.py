##折线图、散点图plot
import matplotlib.pylab as pyl
import numpy as npy
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
c-cyan-青色
r-red
m-magente-品红
g-green
b-blue
y-yellow
k-black
w-white
'''

##线条样式
'''
- 直线
--  虚线
-.  就是-.
:   细小虚线
'''

#点的样式
'''
s--方形
h--六角形
H--六角形
*--星形
+--加号
x--x型
d--菱形
D--菱形
p--五角形
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

#随机数的生成
import numpy as npy

pyl.subplot(3,2,4)#定位图片显示位置(行，列，当前区域位置)
data1 = npy.random.normal(10.0,1.0,1000)#(均数,sigma，个数)
pyl.hist(data1)

#分布直方图hist(x轴参数范围，y轴参数个数)
pyl.subplot(3,1,3)
data2 = npy.random.randint(1,25,1000)#(最小值，最大值，个数)
sty = npy.arange(2,19,4)#设置直方图宽即x轴(最小值，最大值，步长)
pyl.hist(data2,sty)#绘制直方图，sty为直方图格式如上

pyl.show()
