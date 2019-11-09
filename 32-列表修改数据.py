# 列表修改数据

# 修改指定下标数据
names = ['Tom', 'Lily', 'Rose', 'Lily']
names[0] = 'xiaohong'
print(names) # ['xiaohong', 'Lily', 'Rose', 'Lily']

# reverse(): 逆置列表
# 语法: 列表序列.reverse()
names.reverse()
print(names) # ['Lily', 'Rose', 'Lily', 'xiaohong']

# sort(): 排序
# 语法: 列表序列.sort(key=None, reverse=False)
# 注意: reverse表示排序规则，reverse=True降序，reverse=False升序（默认）
names.sort()
print(names) # ['Lily', 'Lily', 'Rose', 'xiaohong']
names.sort(reverse=True)
print(names) # ['xiaohong', 'Rose', 'Lily', 'Lily']
