# 字典常用操作之删除

# del() / del: 删除字典或删除字典中指定键值对。

dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
del dict1['gender']
print(dict1) # {'name': 'Tom', 'age': 20}

# clear(): 清空字典
dict1.clear()
print(dict1) # {}