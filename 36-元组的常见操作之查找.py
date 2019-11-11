# 元组数据不支持修改，只支持查找

# 按下标查找数据
tuple1 = ('aa', 'bb', 'cc', 'dd', 'bb')
print(tuple1[1]) # bb

# index(): 查找某个数据，如果数据存在返回对应的下标，否则报错。
print(tuple1.index('cc')) # 2

# count(): 统计某个数据在当前元组出现的次数
print(tuple1.count('bb')) # 2

# len(): 统计元组中数据的个数
print(len(tuple1)) # 5