# 在Python中，循环分为 while 和 for 两种，最终实现效果相同

# while的语法
# while 条件:
#     条件成立重复执行的代码1
#     条件成立重复执行的代码2
#     ......

num = 0
while num <= 5:
    print(num)
    num += 1

# while的应用
# 应用一： 计算1-100的累加
num1 = 0
i = 1
while i <= 100:
    num1 += i
    i += 1
print(f'1-100的累加: {num1}')

# 应用二： 计算1-100偶数累加和
num2 = 0
i = 1
while i <= 100:
    if i % 2 == 0:
        num2 += i
    i += 1
print(f'1-100偶数累加和: {num2}')

# break和continue
# break 终止此循环
# continue 退出当前一次循环继而执行下一次循环代码
i = 0
while i < 50:
    i += 1
    if i % 2 == 0:
        continue
    if i > 10:
        break
    print(i)

# while循环嵌套应用
# 应用一: 打印星号(正方形)

length = 4
i = 1
while i <= length:
    j = 1
    while j <= length:
        print('*', end='')
        j += 1
    print('', end='\n')
    i += 1

# 应用二: 打印星号(三角形)
length = 4
i = 1
while i <= length:
    j = 1
    len2 = i
    while j <= len2:
        print('*', end='')
        j += 1
    print('', end='\n')
    i += 1

# 应用三: 九九乘法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        r = j * i
        if r < 10:
            r = f'{r} '
        end = '\n' if j == i else ''
        print(f'{j}*{i}={r}   ', end=end)
        j += 1
    i += 1