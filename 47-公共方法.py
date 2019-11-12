# 公共方法

# 函数                      描述
# len()                     计算容器中元素个数
# del或del()                删除
# max()                     返回容器中元素最大值
# min()                     返回容器中元素最小值
# range(start, end, step)   生成从start到end的数字，步长为step，
#                           供for循环使用。
# enumerate()               函数用于将一个可遍历的数据对象(如列表、
#                           元组或字符串)组合为一个索引序列，同时
#                           列出数据和数据下标，一般用在for循环当中

str1 = 'hello python'
print(len(str1)) # 12

list1 = [1, 2, 3, 4]
print(len(list1)) # 4
del(list1[1])
print(list1) # [1, 3, 4]
print(max(list1)) # 4
print(min(list1)) # 1

tuple1 = (1, 2, 3)
print(len(tuple1)) # 3

set1 = {1, 2, 3, 4}
print(len(set1)) # 4

dict1 = {'a': 1, 'b': 2}
print(len(dict1)) # 2
del(dict1['a'])
print(dict1) # {'b': 2}

# range
print(type(range(1, 10, 3))) # <class 'range'>
for i in range(1, 10):
    print(i) # 1 2 3 4 5 6 7 8 9
for i in range(1, 10, 2):
    print(i) # 1 3 5 7 9

# 从0到10, 不包含10
for i in range(10):
    print(i) # 0 1 2 3 4 5 6 7 8 9

# enumerate()
# 语法: enumerate(可遍历对象, start=0)
# start参数用来设置遍历数据的下标的起始值，默认为0
# 返回的结果是元组，元组第一项是索引，第二项是值
list2 = ['a', 'b', 'c', 'd', 'e']
for i in enumerate(list2):
    print(i) # (0, 'a') (1, 'b') (2, 'c') (3, 'd') (4, 'e')
for index, item in enumerate(list2):
    print(f'{index}:{item}') # 0:a 1:b 2:c 3:d 4:e