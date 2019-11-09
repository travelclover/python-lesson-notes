# 列表
# [数据1, 数据2, 数据3, ...]

names = ['Tom', 'Lily', 'Rose', 'Lily']

print(names[2])

# 公共函数len(): 返回列表长度，即列表中数据的个数
print(len(names)) # 4

# idnex(): 返回指定数据所在位置的下标
# 语法: 列表序列.index(数据, 开始位置下标, 结束位置下标)
# 注意: 如果查找的数据不存在则报错
print(names.index('Lily')) # 1
# print(names.index('Dd')) # 找不到就会报错

# count(): 统计指定数据在当前列表中出现的次数
print(names.count('Lily')) # 2
