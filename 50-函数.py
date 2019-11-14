# 函数就是将一段具有独立功能的代码块整合到一个整体并命名，在需要的位置调用这个名称即可完成对应的需求。
# 函数在开发过程中，可以更高效的实现代码重用。

# 定义函数
# def 函数名(参数):
#     代码1
#     代码2
#     ......

# 调用函数
# 函数名(参数)

# 注意
# 1.不同的需求，参数可有可无。
# 2.在python中，函数必须先定义再使用。

def add(num1, num2):
    '''
    求和函数
    :param num1: 参数1
    :param num2: 参数2
    :return: 返回两数之和
    '''
    num = num1 + num2
    printInfo(num)
    return num

def printInfo(text):
    '''
    打印信息函数
    :param text: 需要打印的文字
    '''
    print(text)

num = add(1, 2)
print(num) # 3

help(len) # 查看函数的说明文档
help(add) # 求和函数
