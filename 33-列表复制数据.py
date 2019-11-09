# 列表复制数据

# copy() 函数
names = ['Tom', 'Lily', 'Rose', 'Lily']
names1 = names
names1[0] = 'xiaohong'
print(names) # ['Tom', 'Lily', 'Rose', 'Lily']

names2 = names.copy()
print(names2) # ['xiaohong', 'Lily', 'Rose', 'Lily']
names2[0] = 'huahua'
print(names) # ['xiaohong', 'Lily', 'Rose', 'Lily']
print(names2) # ['huahua', 'Lily', 'Rose', 'Lily']
