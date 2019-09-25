import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy import stats
import pandas as pd

def sinplot(flip=1):
    x = np.linspace(0,14,100)
    for i in range(1,7):
        plt.plot(x,np.sin(x+i*.5)*(7-i)*flip)


sns.set()
##sinplot()

##data = np.random.normal(size=(20,8))+np.arange(8)/2
##sns.set_style("whitegrid")
##sns.boxplot(data=data,palette=sns.color_palette(sns.hls_palette(8,l=.7,s=.9),8))
####sns.violinplot(data)
##sns.despine()

##with sns.axes_style('darkgrid'):
##    plt.subplot(211)
##    sinplot()
##plt.subplot(212)
##sinplot(-1)

##sns.set_context('paper',font_scale=1.5,rc={'lines.linewidth':2.5})#paper/talk/poster/notebook
##plt.figure(figsize=(8,6))
##sinplot()

##plt.plot([0,1],[0,1],sns.xkcd_rgb['pale red'],lw=3)
##plt.plot([0,1],[0,2],sns.xkcd_rgb['medium green'],lw=3)
##plt.plot([0,1],[0,3],sns.xkcd_rgb['denim blue'],lw=3)

##x,y = np.random.multivariate_normal([0,0],[[1,-.5],[-.5,1]],size=100).T
##pal = sns.dark_palette('blue',as_cmap=True)
##sns.kdeplot(x,y,cmap=pal)

##x=np.random.normal(size=100)
##sns.distplot(x,bins=20,fit=stats.gamma,kde=False)

##mean,cov = [0,1],[(1,.5),(.5,1)]
##data = np.random.multivariate_normal(mean,cov,200)
##df = pd.DataFrame(data,columns=['x','y'])
##sns.jointplot(x='x',y='y',data=df,kind='hex',color='k')

##sns.pairplot(sns.load_dataset('iris'))#自带iris花瓣数据库

np.random.seed(sum(map(ord,'regression')))
tips=sns.load_dataset('tips')
titanic=sns.load_dataset('titanic')
##sns.regplot(x='size',y='tip',data=tips,x_jitter=.05)
##sns.regplot(x='total_bill',y='tip',data=tips)
##sns.swarmplot(x='day',y='total_bill',hue='sex',data=tips)
##sns.boxplot(x='day',y='total_bill',hue='sex',data=tips)
##sns.violinplot(x='day',y='total_bill',hue='sex',data=tips,split=True)
##sns.barplot(x='sex',y='survived',hue='class',data=titanic)
##sns.pointplot(x='class',y='survived',hue='sex',data=titanic,
##              palette={'male':'g','female':'m'},
##              markers=['^','o'],linestyles=['-','-.'])
##sns.factorplot(x='day',y='total_bill',hue='smoker',col='time',data=tips,kind='swarm')
##sns.factorplot(x='time',y='total_bill',hue='smoker',col='day',
##               data=tips,kind='box',size=4,aspect=.5)

##np.random.seed(sum(map(ord,'axis_grids')))
##g=sns.FacetGrid(tips,col='time')
##g.map(plt.hist,'tip')

##g=sns.FacetGrid(tips,col='sex',hue='smoker')
##g.map(plt.scatter,'total_bill','tip',alpha=.7)
##g.add_legend()

##g=sns.FacetGrid(tips,row='smoker',col='time',margin_titles='True')
##g.map(sns.regplot,'size','total_bill',color='.5',fit_reg=False,x_jitter=.1)#指定回归的线是否显示

##from pandas import Categorical
##ordered_days = tips.day.value_counts().index
##print(ordered_days)
##ordered_days = Categorical(['Thur','Fri','Sat','Sun'])
##g=sns.FacetGrid(tips,row='day',row_order=ordered_days,
##                size=1.7,aspect=4)
##g.map(sns.boxplot,'total_bill')

##pal = dict(Lunch='seagreen',Dinner='gray')
##g=sns.FacetGrid(tips,hue='time',palette=pal,size=5)
##g.map(plt.scatter,'total_bill','tip',s=50,alpha=.7,linewidth=.5,edgecolor='white')
##g.add_legend()

##pal=dict(Male='red',Female='blue')
##g=sns.FacetGrid(tips,hue='sex',palette=pal,size=5,hue_kws={'marker':['^','v']})
##g.map(plt.scatter,'total_bill','tip',s=100,linewidth=.5,edgecolor='white')
##g.add_legend()

##with sns.axes_style('white'):
##    g=sns.FacetGrid(tips,row='sex',col='smoker',margin_titles=True,size=2.5)
##g.map(plt.scatter,'total_bill','tip',color='#334488',edgecolor='white',lw=.5)
##g.set_axis_labels('Total bill(US Dollars)','Tips')
##g.set(xticks=[10,30,50],yticks=[2,6,10])
##g.fig.subplots_adjust(wspace=.02,hspace=.02)#子图间隔


##g=sns.PairGrid(sns.load_dataset('iris'),vars=['sepal_length','sepal_width'],
##               hue='species',palette='GnBu_d')
####g.map(plt.scatter)
##g.map_diag(plt.hist)#对角为直方图
##g.map_offdiag(plt.scatter,s=50,edgecolor='white')#非对角为散点图
##g.add_legend()

##uniform_data = np.random.rand(3,3)
##print(uniform_data)
##ax = sns.heatmap(uniform_data,vmin=0.2,vmax=0.5)

##normal_data = np.random.randn(3, 3)
##print (normal_data)
##ax = sns.heatmap(normal_data, center=0)

flights = sns.load_dataset("flights")
flights = flights.pivot("month", "year", "passengers")
ax1 = sns.heatmap(flights, annot=True,fmt="d",linewidth=0.5)
##ax2 = sns.heatmap(flights, cmap="YlGnBu",cbar=True)

plt.show()











