# 变量作用域指的是变量生效的范围，主要分为两类：局部变量和全局变量。

# 局部变量
# 所谓局部变量是定义再函数体内部的变量，即只在函数体内部生效。
def testA():
    a = 100
    print(a) # 100

testA()
# print(a) # 报错: name 'a' is not defined
# 局部变量的作用: 在函数体内部，临时保存数据，即当函数调用完成后，则销毁局部变量。

# 全局变量
# 所谓全局变量，指的是在函数体内、外部都能生效的变量。
A = 99
def printA():
    print(A) # 99
printA()
print(A) # 99

# 修改全局变量
def printA2():
    # global 关键字声明A是全局变量
    global A
    A = 101
    print(A)
printA2() # 101
printA() # 101