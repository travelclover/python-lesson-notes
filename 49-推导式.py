# 列表推导式
# 作用: 用一个表达式创建一个有规律的列表或控制一个有规律列表。
# 列表推导式又叫列表生成式。

list1 = [i for i in range(10)]
print(list1) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list2 = [(i, j) for i in range(1, 3) for j in range(3)]
print(list2) # [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# 列表带if的推导式
list3 = [i for i in range(1, 10) if (i % 2 == 0)]
print(list3) # [2, 4, 6, 8]

# 字典推导式
# 作用: 快速合并列表为字典或提取字典中目标数据。
dict1 = {i: i ** 2 for i in range(1, 5)}
print(dict1) # {1: 1, 2: 4, 3: 9, 4: 16}
list4 = [['name', 'age'], ['Tom', 29]]
dict2 = {list4[0][i]: list4[1][i] for i in range(len(list4[0]))}
print(dict2) # {'name': 'Tom', 'age': 29}

# 字典带if推到式
dict3 = {key: value for key, value in dict2.items() if key == 'name'}
print(dict3) # {'name': 'Tom'}

# 集合推导式
list5 = [1, 2, 1]
set1 = {i ** 2 for i in list5}
print(set1) # {1, 4}