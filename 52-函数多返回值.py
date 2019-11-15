# 函数多返回值

def test():
    return 1, 2 # 返回的是元组

a = test()
print(a) # (1, 2)

def test1():
    return (10, 20)

a1 = test1() # (10, 20)
print(a1)