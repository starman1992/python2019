import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 定义横纵坐标的中文字符格式
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

df = pd.read_excel('movie_data.xlsx',index_col=[0])
# df['评分登记']=pd.cut(df['评分'],[0,3,5,7,9,10],labels=['E','D','C','B','A'])
# bins=np.percentile(df['投票人数'],[0,20,40,60,80,100])
# df['热门程度']=pd.cut(df['投票人数'],bins,labels=['E','D','C','B','A'])

##1、画每个产地电影数量的柱状图
data1=df['产地'].value_counts()
x1=data1.index
y1=data1.values

plt.figure(figsize=(10,6))
plt.bar(x1,y1,color='g')
plt.title('个国家或地区电影数量',fontsize=18)
plt.xlabel('国家或地区',fontsize=18)
plt.ylabel('电影数量',fontsize=18)
plt.tick_params(labelsize=14)
plt.xticks(rotation=90)

for a,b in zip(x1,y1):
   plt.text(a,b+10,b,ha='center',va='bottom',fontsize=10)#ha表左右居中，va表在特定位置的上下
plt.grid()# 网格线

##2、画每个年代电影变化数量
data2=df[df['年代']>=1900]['年代'].value_counts()
data2=data2.sort_index()[:-1] #2016年数据不全
x2=data2.index.tolist()#不tolist报错
y2=data2.values

plt.figure(figsize=(10,6))
plt.plot(x2,y2)
plt.title('每年电影数量',fontsize=20)
plt.ylabel('电影数量',fontsize=18)
plt.xlabel('年份',fontsize=18)

for a,b in zip(x2[::10],y2[::10]):
    plt.text(a,b+10,b,ha='center',va='bottom',fontsize=10)
plt.annotate('2012年达到最大值',xy=(2012,data2[2012]),xytext=(2015,2100),\
             arrowprops=dict(facecolor='yellow',edgecolor='black'))#标注极值点
plt.text(1980,1000,'电影数量开始快速增长',ha='center')

##3、画各电影时长占比的饼图
data3=pd.cut(df['时长'],[0,60,90,120,1000]).value_counts()
y3=data3.values
y3=y3/sum(y3)

plt.figure(figsize=(7,7))
plt.title('电影时长占比',fontsize=15)
patches,l_text,p_text=plt.pie(y3,labels=data3.index,autopct='%.1f%%',colors='bygr')
for i in p_text:
    i.set_size(15)
    i.set_color('w')
for i in l_text:
    i.set_size(15)
    i.set_color('r')
plt.legend()

##4、画评分的分布直方图
data4=df['评分'].sort_values()
plt.figure(figsize=(10,6))
n1,bins1,patches1=plt.hist(df['评分'],bins=80,edgecolor='k',alpha=0.5) # density=1
for i in range(80):
    if bins1[i] > data4.mean():
        mean_point=i
        break
for i in range(80):
    if bins1[i] > data4[int(len(data4)/2)]:
        median_point = i
        break

for a,b in zip(bins1[::8],n1[::8]):
    plt.text(a,b+50,b,ha='center',va='bottom',fontsize=10)
plt.annotate('众数是{}'.format(bins1[n1.argmax()]),xy=(bins1[n1.argmax()],n1.max()),\
            xytext=(bins1[n1.argmax()]+0.5,n1.max()+100),\
            arrowprops=dict(facecolor='yellow',edgecolor='black'))#标注极值点
plt.annotate('均值是{}'.format(round(data4.mean(),2)),xy=(bins1[mean_point],n1[mean_point]),\
            xytext=(bins1[mean_point]-1,n1[mean_point]+50),\
            arrowprops=dict(facecolor='yellow',edgecolor='black'))
plt.annotate('中位数是{}'.format(round(data4[int(len(data4)/2)],2)),xy=(bins1[median_point],n1[median_point]),\
            xytext=(bins1[median_point]-0.6,n1[median_point]+150),\
            arrowprops=dict(facecolor='yellow',edgecolor='black'))
##画指示箭头annotate(要写的文字,xy描述点的坐标,xytext描述话的坐标,arrowprops箭头的格式)

##5、双轴图画法
from scipy.stats import norm  # import matplotlib.mlab as mlab在用到mlab.normpdf会报错

fig1=plt.figure(figsize=(10,8))
ax1=fig1.add_subplot(111)
#直方图返回值n表示直方图向量，bins表示各个区间范围，patches表示每个bins包含的数据
n2,bins2,patches2=ax1.hist(df['评分'],bins=40,color='m',edgecolor='k')
ax1.set_ylabel('电影数量',fontsize=15)
ax1.set_xlabel('评分',fontsize=15)
ax1.set_title('频数分布图',fontsize=20)
mu=df['评分'].mean()
sigma=df['评分'].std()
y5 = norm.pdf(bins2,mu,sigma)
ax2=ax1.twinx()
ax2.plot(bins2,y5,'b--')
ax2.set_ylabel('概率分布',fontsize=15)

##6、绘制电影时长及评分散点图
x6=df['时长']
y6=df['评分']
plt.figure(figsize=(10,6))
plt.scatter(x6,y6,color='c',marker='.')
plt.title('电影时长与评分散点图',fontsize=20)
plt.xlabel('时长',fontsize=18)
plt.ylabel('评分',fontsize=18)

##7、画箱图
##import seaborn as sns
##sns.boxplot(x='产地',y='评分',data=df)

##dd1=df[df.产地=='中国大陆']['评分']
##dd2=df[df.产地=='中国台湾']['评分']
##plt.boxplot([dd1,dd2],labels=['中国大陆','中国台湾']

plt.figure(figsize=(8,8))
data7=df[['产地','评分']]
data7=data7.groupby('产地')['评分']

gname=[]
ggroup=[]
for name,group in data7:
    gname.append(name)
    ggroup.append(group)
plt.boxplot(ggroup,labels=gname,whis=2,flierprops={'marker':'o','markerfacecolor':'r','color':'k'},\
            patch_artist=True,boxprops={'color':'k','facecolor':'#9999ff'},vert=False)
plt.xticks(rotation=90)
ax3=plt.gca()
ax3.patch.set_facecolor('grey')
ax3.patch.set_alpha(0.3)
plt.title('电影评分箱线图',fontsize=20)
plt.tight_layout()
plt.subplots_adjust(top=0.8,bottom=0.2,left=0.1,right=0.9,hspace=0.1,wspace=0.1)
# 子图上下左右边的位置，子图间上下或左右的宽度

##8、画热力图
import seaborn as sns
data8=df[['投票人数','评分','时长']]
# result=pd.plotting.scatter_matrix(data8[::100],diagonal='kde',color='k',\
                                  # alpha=0.8,figsize=(8,8),range_padding=0.1) 
##kde对角线显示集核密度估计,hist对角线显示分布直方图
corr=data8.corr().abs()
# fig2=plt.figure(figsize=(6,6))
ax4=sns.heatmap(corr,annot=True,vmin=0,vmax=1,yticklabels='auto',\
                annot_kws={'size':13,'weight':'bold'},linewidths=0.5)

plt.show()

##df.to_excel('movie_data.xlsx')




















