# 列表删除数据

# del()
# 语法: del 目标 或者 del(目标)
names = ['Tom', 'Lily']
# del names[0]
del(names[0])
print(names) # [;Lily]

# pop(): 删除指定下标的数据（默认最后一个），并返回该数据
# 语法: 列表序列.pop(下标)
names2 = ['Tom', 'Lily', 'Rose']
print(names2.pop()) # Rose
print(names2) # ['Tom', 'Lily']
print(names2.pop(0)) # Tom
print(names2) # ['Lily']

# remove(): 移除列表中某个数据的第一个匹配项
# 语法: 列表序列.remove(数据)
names3 = ['Tom', 'Lily', 'Rose', 'Lily']
names3.remove('Lily')
print(names3) # ['Tom', 'Rose', 'Lily']

# clear(): 清空列表
names3.clear()
print(names3) # []
