# 集合删除数据

# remove() 删除集合中的指定数据，如果数据不存在则报错。
s1 = {1, 2, 3}
s1.remove(1)
print(s1) # {2, 3}
# s1.remove(10) # 报错

# discard() 删除集合中的指定数据，如果数据不存在也不会报错。
s1.discard(10)
print(s1) # {2, 3}

# pop() 随机删除集合中的某个数据，并返回这个数据。
s2 = {3, 2, 1, 4, 5}
delNum = s2.pop()
print(delNum)
print(s2)