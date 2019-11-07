# 条件语句
# 语法
# if 条件:
#     条件成立执行的代码1
#     条件成立执行的代码2
#     ......
# elif 条件2:
#     条件2成立执行的代码1
#     条件2成立执行的代码2
# else:
#     条件不成立执行的代码1
#     条件不成立执行的代码2
#     ......

age = input('请输入年龄:')
age = int(age)

if age <= 18:
    print('未成年')
elif age >= 60:
    print('老年人')
elif 30 <= age <= 40:
    print('正是壮年')
else:
    print('成年了')

print('检测完毕！')
