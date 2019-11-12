# 公共操作之运算符

# 运算符        描述                支持的容器类型
# +             合并                字符串、列表、元组
# *             复制                字符串、列表、元组
# in            元素是否存在        字符串、列表、元组、字典
# not in        元素是否不存在      字符串、列表、元组、字典

str1 = 'hello'
str2 = ' python'
print(str1 + str2) # hello python
print(str1 * 2) # hellohello
print('o' in str1) # True

list1 = [1, 2]
list2 = [3, 4]
print(list1 + list2) # [1, 2, 3, 4]
print(list1 * 2) # [1, 2, 1, 2]
print(2 in list1) # True

tuple1 = (1, 2)
tuple2 = (2, 3)
print(tuple1 + tuple2) # (1, 2, 2, 3)
print(tuple1 * 2) # (1, 2, 1, 2)
print(2 in tuple1) # True

dict1 = {'a': 1}
print('a' in dict1) # True
print(1 in dict1) # False