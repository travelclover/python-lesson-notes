# startswith(): 检查字符串是否以指定子串开头，是则返回True,否则返回False。
# 如果设置开始和结束位置下标，则在指定范围内检查
# 语法: 字符串序列.startswith(子串, 开始位置下标, 结束位置下标)
str1 = 'hello python'
print(str1.startswith('py')) # False
print(str1.startswith('py', 6)) # True

# endsswith(): 检查字符串是否以指定子串结尾，是则返回True,否则返回False。
# 如果设置开始和结束位置下标，则在指定范围内检查
# 语法: 字符串序列.endswith(子串, 开始位置下标, 结束位置下标)
print(str1.endswith('lo')) # False
print(str1.endswith('lo', 1, 5)) # True