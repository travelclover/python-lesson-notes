# 字典常用操作之查找

# key值查找
# 如果当前查找的key存在，则返回对应的值，否则报错
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
print(dict1['name']) # Tom

# get()
# 语法: 字典序列.get(key, 默认值)
# 注意: 如果当前查找的可以不存在则返回第二个参数(默认值)，如果省略第二个参数，则返回None.
print(dict1.get('name')) # Tom
print(dict1.get('names')) # None

# keys(): 查找字典中所有的key，返回一个可迭代对象
print(dict1.keys()) # dict_keys(['name', 'age', 'gender'])
print(type(dict1.keys())) # <class 'dict_keys'>

# values(): 查找字典中所有的值，返回一个可迭代对象
print(dict1.values()) # dict_values(['Tom', 20, '男'])
print(type(dict1.values())) # <class 'dict_values'>

# items(): 查找字典中所有的键值对，返回一个可迭代对象，里面的数据都是元组
print(dict1.items()) # dict_items([('name', 'Tom'), ('age', 20), ('gender', '男')])
print(type(dict1.items())) # <class 'dict_items'>