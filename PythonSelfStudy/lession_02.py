#!/usr/bin/python
# -*- coding: UTF-8 -*-
print("content1")
print("content2")
print("""content3 content4""")
if True:
    print("True")
else:
    print("false")

# this is a comment
'''
these are comments
these are comments
these are comments
'''
x = '$'
y = 'b'
print('------')
# not change line print
print(x * 5, end='')  # python 3
print(y)

counter = 100  # 赋值整形变量

a, b, c = 11, 22, 'hao'  # 多个变量赋值
print(a, end=''), print(b, end=''), print(c)

# Python有五个标准的数据类型
# Numbers（数字）
# String（字符串）
# List（列表） list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
# Tuple（元组）
# Dictionary（字典）

print('################')
str = 'test python '
print(str)
print(str[0])
print(str[2:5])
print(str[2:])
print(str * 2)
print(str + 'add string abc')


print('######## Python 列表 ########')
list = ['runoob', 789, 2.23, 'joint', 70.2]
list_2 = ['123', 'HoC']
print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(list_2 * 2)
print(list + list_2)

print('######## Python 元组 ########')
tuple = ('runoob', 786, 2.23, 'john', 70.2)
print(tuple)
list[1] = 888
print(list)
# 元组是不允许更新的。而列表是允许更新
# tuple[1]=999

print('######## Python 字典 ########')
dict = {}
dict['one'] = 'this is one'
dict[2] = 'this is two'

# tinydict = {'name1': 'zod', 'name3': 'Luxifa', 'name2': 'Aerfa'}
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print(dict)
print(dict['one'])
print(dict[2] )
print(tinydict)
print(tinydict.keys())
print(tinydict.values())

a = '12';
print(a)
print(type(a))
print(int(a,16))
print(int(a,10))
print(int(a))

