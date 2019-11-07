# 字符串的常用操作方法有查找、修改和判断三大类

# 查找
# 所谓字符串查找方法即是查找子串在字符串中的位置或出现的次数

# find(): 检测某个子串是否包含在这个字符串中
# 如果在则返回这个子串开始的位置下标，否则返回-1
# 语法：字符串序列.find(子串, 开始位置下标, 结束位置下标)
# 注意：开始和结束位置下标可以省略，表示在整个字符串序列中查找

str1 = 'I love python very much'
print(str1.find('love')) # 2
print(str1.find('love', 10, 15)) # -1

# index(): 检测某个子串是否包含在这个字符串中，
# 如果在则返回这个子串开始的位置下标，否则报异常
# 语法：字符串序列.find(子串, 开始位置下标, 结束位置下标)
# 注意：开始和结束位置下标可以省略，表示在整个字符串序列中查找
print(str1.index('love')) # 2
# print(str1.index('love1')) # 报异常

# count(): 返回某个子串在字符串中出现的次数
print(str1.count('o')) # 2
print(str1.count('my')) # 0

# rfind(): 和find()功能相同，但查找方向为右侧开始。
# rindex(): 和index()功能相同，但查找方向为右侧开始。
print(str1.find('o')) # 3
print(str1.rfind('o')) # 11