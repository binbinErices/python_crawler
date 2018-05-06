#!usr/bin/env python  
# -*- coding: UTF-8 -*- 
""" 
@author:binbinzhang
@file: 1.py.py 
@time: 2018/05/05 
@email:binbin_Erices@163.com
@function：python数据分析基础numpy
"""
import numpy as np


#生成指定维数的多位数据 两行三列
data = np.random.rand(2,3)

print(data)
print(type(data))

# shape各维度大小
# ndim维度个数
l = range(10)
data = np.array(l)

print(data)
print(data.ndim)
print(data.shape)  #(10,)

# 嵌套序列
l2 = [range(10),range(10)]
data = np.array(l2)

print(data)
print(data.shape) #(2, 10)
print(data.ndim)

# np.zeros
zeros_arr = np.zeros((3,4))
print(zeros_arr)
print(type(zeros_arr))

 # arange
data = np.arange(10)
print(data)

# ndarray数据类型 dtype 与 atype
zeros_float_arr = np.zeros((3,4),dtype=np.float64)
print(zeros_float_arr)
print(zeros_float_arr.dtype)

zeros_int_arr = zeros_float_arr.astype(np.int32)
print(zeros_int_arr)
print(zeros_int_arr.dtype)

# 矢量与矢量运算
arr = np.array([[1,2,3],
               [4,5,6]])
print("元素相乘：")
print(arr*arr)
print("矩阵相加：")
print(arr+arr)

# 矢量与标量的运算
print(1./arr)
print(3.*arr)

# 索引与切片
# 一维数组
arr1 = np.arange(10)
print(arr1)
print(arr1[2:5])

# 多维数组
arr2 = np.arange(12).reshape(3,4)
print(arr2)
print(arr2[1])
print(arr2[1:, 2:])

# 条件索引
arr_data = np.arange(9).reshape(3,3)
print(arr_data)
arr_year = np.array([[2000,2011,2004],
                     [2005,2003,2007],
                     [2008,2016,2018]])
arr_filter = arr_data[arr_year >= 2011]
print(arr_filter)

# 多个条件
arr_filter = arr_data[(arr_year >= 2011)&(arr_year % 2 == 0)]
print(arr_filter)

# 转置
arr3d = np.random.rand(2,3,4)
print(arr3d)
print(arr3d.transpose())

# 通用函数
# ceil向上取整
# floor向下取整
# rint四舍五入
# isnan
arr_1 = np.random.rand(2,3)
print(arr_1)
print(np.ceil(arr_1))
print(np.floor(arr_1))
print(np.rint(arr_1))
print(np.isnan(arr_1))  #[[False False False]

#numpy中有一些常用的用来产生随机数的函数，randn()和rand()就属于这其中。 
#numpy.random.randn(d0, d1, …, dn)是从标准正态分布中返回一个或多个样本值。 
#numpy.random.rand(d0, d1, …, dn)的随机样本位于[0, 1)中。

# np.where(condition,x,y) x if condition else y 满足执行X 不满足执行y
arr_2 = np.random.randn(3,3)
print(arr_2)
print(np.where(arr_2 > 0, 1, -1))

# 常用的统计方法
arr_3 = np.arange(12).reshape(3,4)

print(arr_3)
print(np.sum(arr_3))
print(np.sum(arr_3,axis=0)) # 纵向方向统计
print(np.sum(arr_3,axis=1)) # 横向方向统计


# np.all 全部满足条件
# np.any 至少有一个元素满足条件
# np.unique 找到唯一值并返回排序结果
arr_4 = np.arange(12).reshape(3,4)

print(arr_4)
print(np.all(arr_4>3))  #False
print(np.any(arr_4>10)) #True
arr_4 = np.arange(12).reshape(3,4)

arr_5 = np.array([[3,2,4],
                  [7,4,6]])
print(arr_5)
print(np.unique(arr_5)) #[2 3 4 6 7]


'''
建模基础;
分类
回归
聚类
时序分析
'''



