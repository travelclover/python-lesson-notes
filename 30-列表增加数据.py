# 列表增加数据

names = ['Tom', 'Lily']

# append(): 列表末尾追加数据
# 语法: 列表序列.append(数据)
# 注意: 如果追加的数据是一个序列，则追加整个序列到列表
names.append('xiaoming')
print(names) # ['Tom', 'Lily', 'xiaoming']
names.append(['xiaohong', 'xiaohua'])
print(names) # ['Tom', 'Lily', 'xiaoming', ['xiaohong', 'xiaohua']]

# extend(): 列表结尾追加数据，如果数据是一个序列，则将这个序列的数据逐一添加到列表
# 语法: 列表序列.extend(数据)
names2 = ['xiaohua']
names2.extend('Tom') # ['xiaohua', 'T', 'o', 'm']
print(names2)
names2.extend(['Lily', 'xiaohong'])
print(names2) # ['xiaohua', 'T', 'o', 'm', 'Lily', 'xiaohong']

# insert(): 指定位置新增数据
# 语法: 列表序列.insert(位置下标, 数据)
names3 = ['Tom', 'Lily']
names3.insert(1, 'huahua')
print(names3) # ['Tom', 'huahua', 'Lily']
