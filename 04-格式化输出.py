# %s 字符串
# %d 有符号的十进制整数
# %f 浮点数

age = 18
name = 'travelclover'
height = 1.75
print('今年我的年龄是%d岁' % age)
print('今年我的年龄是%04d岁' % age)
print('今年我的名字是%s' % name)
print('今年我的身高是%f' % height)
print('今年我的身高是%.2f' % height) # 保留2位小数

print('今年我的名字是%s, 明年我的年龄是%d岁, 今年我的身高是%f' % (name, age + 1, height))
print('今年我的名字是%s, 明年我的年龄是%s岁, 今年我的身高是%s' % (name, age + 1, height))

# f格式化 语法 f'{表达式}' Python3.6中新增的格式化方法
print(f'今年我的名字是{name}, 明年我的年龄是{age + 1}岁, 今年我的身高是{height}')
