# 循环可以和else配合使用，else下方缩进的代码指的是 当循环正常结束之后要执行的代码
# 所谓else指的是循环正常结束之后要执行的代码，
# 即如果是break终止循环的情况，else下方缩进的代码将不执行

# 语法:
# while 条件:
#     条件成立重复执行的代码
# else:
#     循环正常结束之后要执行的代码

i = 1
while i <= 10:
    print(i)
    i += 1
    if i > 5:
        break
else:
    print('else')
print('finished')