# 拆包元组数据
def return_num():
    return 100, 200

num1, num2 = return_num()
print(f'num1={num1}, num2={num2}') # num1=100, num2=200

# 拆包字典数据
# 对字典进行拆包，取出来的是字典的key
dict1 = {'name': 'Tom', 'age': 20}
a, b = dict1
print(a) # name
print(b) # age
print(dict1[a]) # Tom
print(dict1[b]) # 20