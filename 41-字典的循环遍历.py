# 字典的循环遍历

# 遍历字典的key
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
for key in dict1.keys():
    print(f'{key}: {dict1.get(key)}')

# 遍历字典的value
for value in dict1.values():
    print(value)

# 遍历字典的键值对
for item in dict1.items():
    print(f'{item[0]}: {item[1]}')
for key, value in dict1.items():
    print(f'{key}: {value}')