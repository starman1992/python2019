from pandas import Series,DataFrame
import pandas as pd
import datetime
import numpy as np

a=datetime.date(2019,7,24)
##print(a,a.year,a.month,a.day)

b=datetime.time(9,10,34)
##print(b,b.hour,b.minute,b.second)

c=datetime.datetime.now()
d=datetime.timedelta(10)#默认天
e=c+d
##print(c,d,e)

f = a.strftime('%Y/%m/%d')
##print(f)#日期转字符串
##print(a.strftime('%W'))#第几周
##print(datetime.datetime.strptime(f,'%Y-%m-%d'))
g = pd.to_datetime(f)

index1=pd.date_range('2019/7/1','2019/7/20',freq='D')#构造时间，设定频率
#D自然日  B工作日  M每月最后一个日历日  BM每月最后一个工作日
#H每小时  T每分钟  S每秒  A-JAN,A-FEB指定月份最后一个日历日
index2=pd.date_range(start='2019/7/1',periods=20)#向后构造时间，设定个数
index3=pd.date_range(end='2019/7/1',periods=20)#向前构造时间，设定个数
index4=pd.date_range(start='2019/7/1 15:11:34',periods=20,normalize=True)#去掉时间
index5=pd.date_range(start='2019/7/1',periods=20,freq='2H20min38S')
s1=pd.Series(np.arange(20),index=index1)
s2=s1.shift(2)#值往下调(有NaN)
s3=s1.shift(2,freq='D')#日期按日历日往上调2天
s4=s1.shift(2,freq='M')#日期按日历月往上调2个月

#重采样
s5=s1.resample('M').mean()#改按月采样
s6=s1.resample('5D',closed='right',label='right').mean()#改5天采样，从右数
s7=s1.resample('5D',closed='left',label='left').mean()#改5天采样，从左数
s8=s1.resample('5D',closed='right',label='right',loffset='-1D').mean()#改5天采样，从左数
s9=s1.resample('D').ffill(7)#对于零散型的序列，进行升采样填充7个缺失值
print(s7)
