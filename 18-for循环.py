# for 循环
# 语法:
# for 临时变量 in 序列:
#     重复执行的代码1
#     重复执行的代码2
#     ......

str1 = 'hello python'
arr1 = [1, 2, 3, 4]

for i in str1:
    print(i)

for i in arr1:
    print(i)

for i in str1:
    print(i)
    if i == ' ':
        break

print('--------------')

for i in str1:
    if i == ' ':
        continue
    print(i)