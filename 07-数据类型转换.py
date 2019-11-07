# 数据类型转换函数
# int(x [,base])            将x转换为一个整数
# float(x)                  将x转换为一个浮点数
# str(x)                    将x转换为字符串
# eval(str)                 用来计算在字符串中的有效Python表达式，并返回一个对象
# tuple(s)                  将序列s转换为一个元组
# list(s)                   将序列s转换为一个列表
# complex(real [,image])    创建一个复数，real为实部，imag为虚部
# repr(x)                   将对象x转换为表达式字符串
# chr(x)                    将一个整数转换为一个Unicode字符
# ord(x)                    将一个字符转换为它的ASCII整数值
# hex(x)                    将一个整数转换为一个十六进制字符串

i = input('请输入：')
print(int(i))
print(type(int(i)))

print(float(i))
print(type(float(i)))

print(tuple([1, 2, 3]))

print(list((1, 2, 3)))

print(eval('1.1'))
