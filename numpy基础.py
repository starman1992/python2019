import numpy as np
data1 = np.array([2,3,4])
data2 = np.array([[1,2,3],[4,5,6]])
a3 = 7,8,9
data3 = np.array(a3)
data4 = np.arange(8)
data5 = np.ones((3,4),dtype='float64')
data6 = np.zeros((3,4))
data7 = np.empty((2,3,4))#高维数组
data9 = np.array([2.3,7.5,5.6,9.8])
data13 = np.arange(8,16).reshape(2,4)

data8 = data5.astype('string_')
data10 = data9.astype('int32')
data11 = data4.reshape((2,-1))#-1这里表示自计算的默认除数
data12 = data11.ravel()#平摊
data14 = np.concatenate([data11,data13],axis=0)
#按列堆叠，相当于arr+arr，np.vstack，vertical
data15 = np.concatenate([data11,data13],axis=1)
#按行堆叠，相当于元素内拼接，np.hstack，horizontal

data16 = np.split(data14,2)#横切均分
data17 = np.array_split(data14,3)#横切不均分array_split
data18 = np.split(data14,(3,))#在位置3横切一刀
data19 = np.split(data14,[1,3])#在位置1和3切分
data20 = np.split(data14,2,axis=1)#纵切均分
data21 = np.array_split(data14,[1,3],axis=1)#纵切不均分

data22 = data14.transpose((1,0))#转置  或用data14.T

data23 = np.random.randint(100,200,size=(5,4))
data24 = np.random.randn(2,3)#生成一个标准正态分布矩阵
data25 = np.random.normal(0,3,size=(5,4))#生成一个以0为均值3为标准差的数组
data26 = np.random.uniform(0,3,size=(5,4))#生成一个0-3内的均匀分布
data28 = np.random.poisson(2,size=(5,4))#生成一个lambda为2的泊松分布
data26 = np.random.permutation(data14)#随机行间排序（行内不变）不改变原数组
data27 = np.random.shuffle(data14)#随机行间排序（行内不变）直接改变原数组且没有返回值

data28 = data14[:,1]#取所有行的第2列元素
data29 = data14[:,1:2]#取所有行的第2列元素单独形成一个列表

fruits = np.array(['apple','pear','pear','orange'])
cond = np.array([1,0,1])

#np.abs取绝对值   np.square取平方   np.minimum   np.maximum   np.modf取其个位数和小数第一位
#np.sum(1)第一列求和   np.mean(axis=1)每行求平均  np.std()标准差
#np.cumsum累积每行求和    np.cumprod(1)第一列累积求积   (arr>0).sum()大于0求和
#np.sort排序  np.unique()去重返回唯一值

##print(data1,"\n",data2,"\n",data3,'\n',data4)
##print(data5,str(data5.ndim),str(data7.size))
##维数，元素数
##print(data14[fruits=='pear',:3])

##print(np.where(cond,data1,data3))#√选data1中的数，×选data2中的数
##print(np.where(data23>180,'优秀',\
##               np.where(data23<130,'不合格','合格')))
print(data20,'\n',data21)











