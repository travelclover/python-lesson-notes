# 在python中，值是靠引用来传递的。
# 我们可以用id()来判断两个变量是否为同一个值的引用。
# 我们可以将id值理解为那块内存的地址标识。

a = 10
b = a
print(id(a)) # 140724282188912
print(id(b)) # 140724282188912
a = 11
print(id(a)) # 140724282188944
print(id(b)) # 140724282188912

list1 = [1, 2]
list2 = list1
list3 = list1
print(id(list1)) # 1894426523016
print(id(list2)) # 1894426523016
list1 = [3, 4]
print(list1) # [3, 4]
print(list2) # [1, 2]
print(id(list1)) # 1894426713672
print(id(list2)) # 1894426523016
list3[0] = 5
print(list1) # [3, 4]
print(list2) # [5, 2]
print(list3) # [5, 2]
print(id(list1)) # 1894426713672
print(id(list2)) # 1894426523016
print(id(list3)) # 1894426523016