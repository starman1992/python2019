from pandas import Series,DataFrame
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

##pd.read_csv('路径')
##pd.read_table('路径',sep=',')
##pd.read_csv(open('路径'),index_col=['xx','yy'],names=['xx','yy'])#设置索引列,表头（如果没有表头则设置为header=None）
##pd.read_csv(open('路径'),skiprows=[0,5],nrows=2,usecols=['xx','yy'])#跳过第0,5行，显示2行和第xx.yy列
##pd.read_tabl(open('txt',sep='re'))
##df.to_csv('xx.csv',index=False)#储存到csv,没有数字index
##pd.read_json('路径')
##pd.read_excel('路径',sheet_name='sheet1')


df1 = DataFrame({
    'name':['张三','李四','王五','小明'],
    'sex':['female','female','male','male'],
    'city':['深圳','上海','深圳','上海'],
    'year':['2001','2004','2003','2002']})
                
df2 = df1.append({
    'city':'武汉',
    'name':'小李',
    'sex':'male',
    'year':'2007'
    },ignore_index=True)#忽略索引值新增
df2['cash'] = [92,83,78,69,82]#这里只有cash列是数组，所以计算默认这唯一列
##print(df2)

grouped = df2['cash'].groupby(df2['sex'])
df2['bill'] = [123,342,186,256,525]
df2['year'] = df2['year'].astype(int)#把字符串转成float或者int
##print(grouped.sum())
##for name,group in df2.groupby(df2['sex']):
##    print(name)
##    print(group)

#按列名分组
##sex_mean = df2.groupby('sex').mean()
##sex_mean.plot(kind='bar',)
##plt.show()

#按字典分组，分组前需要改index为dict1的格式
##dict1 = {'a':'one','A':'one','b':'two','B':'two'}
##xx.groupby(dict1).sum()

#按函数分组
##def jug(x):
##    if x>=0:
##        return 'a'
##    else:
##        return 'b'
##xx[3].gruopby(xx[3],map(jug)).sum()

#聚合
##df3=df2.groupby(['sex','city'])['cash'].agg([('cash_mean','mean'),'std','count'])
###对mean进行取名
##df4=df2.groupby(['sex'],as_index=False)['cash','bill'].agg({'cash':['sum','mean'],'bill':'mean'})
###对不同数据列分别做不同操作,分组不作为索引
##print(df4)

#分组运算
def top(x,n=5):
    return x.sort_values(by='cash',ascending=False)[-n:]
#降序排列，取最后5个值
##f = lambda x:x.fillna(x.mean())
##df.groupby('sex').apply(f)
#对数据中na的值进行分组填充
def not_null_count(column):#全局看该字段缺失个数
    column_null=pd.isnull(column)
    null=column[column_null]
    return len(null)

def re_name(row):#全局中，单列内容改名
    if pd.isnull(row['xxx']):
        return "Unknown"
    if row['xxx'] == 'a':
        return "b"
#row['new_name']= row.apply(rename,axis=1)新建列

##tips.pivot_table(values='值',index='行索引',columns='列索引',aggfunc='sum')#默认平均值
##tips.pivot_table(values='值',index='行索引',columns='列索引',aggfunc='sum',margins='ALL')#ALL表汇总

##['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age',
## 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']

data = pd.read_csv('titanic_train.csv')
head = data.columns.tolist()
##titanic_surv = data[data['Survived'] == 1]
def re_name(age):
    if pd.isnull(age):
        return "unknown"
    if age >= 18:
        return "adult"
    if age < 18:
        return "youth"

##new = data[["Survived"]].groupby(data['Age'].map(re_name)).mean()

##print(new)
##pclass_con = {1:'First',2:'Second',3:'Third'}
##data = data.set_index('Pclass')
##print(data['PassengerId'].groupby(pclass_con).count())

##print(data['Embarked'].unique())
##
##age_labels = data["Age"].apply(re_name)
##data["age_labels"] = age_labels
####age_gruop_surv = data.pivot_table(index="age_labels",values=["Survived"])
##age_gruop_surv = data[['Survived']].groupby(data['age_labels']).mean()#不多加个[]会比数据透视表少表头survived
####print(titanic_surv)
##print(age_gruop_surv)
##def add_A(x):
##    return "A" + str(x)
##def slice_A(x):
##    return float(x.split("A",1)[1])
##age_gruop_surv_A = age_gruop_surv.applymap(add_A)
##print(age_gruop_surv_A)
##age_gruop_surv_slice_A = age_gruop_surv_A.applymap(slice_A)
##print(age_gruop_surv_slice_A[['Survived']].applymap(lambda x : "%.3f"%x))

##df=data.groupby(['Sex','Embarked'])['Fare','Age'].agg({'MEAN':'mean', 'SUM':'sum'})
##print(df)


