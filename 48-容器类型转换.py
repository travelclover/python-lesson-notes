# 容器类型转换

tuple1 = (1, 2, 3)
list1 = [1, 3, 2]
set1 = {1, 2, 3}

# tuple() 将某个序列转换成元组
print(tuple(list1)) # (1, 2, 3)
print(tuple(set1)) # (1, 2, 3)

# list() 将某个序列转换成列表
print(list(tuple1)) # [1, 2, 3]
print(list(set1)) # [1, 2, 3]

# set() 将某个序列转换成集合
print(set(tuple1)) # {1, 2, 3}
print(set(list1)) # {1, 2, 3}