# 1位置参数
# 调用函数时根据函数定义的参数位置来传递参数。
# 注意：传递和定义参数的顺序及个数必须一致。
def user_info(name, age, gender):
    print(f'您的名字是{name}，年龄是{age}，性别是{gender}')
user_info('Tom', 20, '男')

# 2关键字参数
# 函数调用，通过“键=值”形式加以指定。可以让函数更加清晰、容易使用，同时也清除了参数的顺序需求。
user_info('Rose', gender='女', age=10) # 您的名字是Rose，年龄是10，性别是女

# 3缺省参数
# 缺省参数也叫默认参数，用于定义函数，为参数提供默认值，调用函数时可不传该默认参数的值。
# 注意：所有位置参数必须出现在默认参数前，包括函数定义和调用。
def user_info2(name, age, gender='男'):
    print(f'{name}, {age}, {gender}')
user_info2('Tom', 24) # Tom, 24, 男

# 4不定长参数
# 不定长参数也叫可变参数，用于不确定调用的时候会传递多少个参数（不传参也可以）的场景。此时，可用包裹（packing）位置参数，或者包裹关键字参数，来进行参数传递，会显得非常方便。

# 包裹位置传递
# 注意：传进的所有参数都会被args变量收集，它会根据传进参数的位置合并为一个元组（tuple），args是元组类型。
def user_info3(*args):
    print(args)
user_info3('Tom') # ('Tom',)
user_info3('Tom', 34) # ('Tom', 34)
user_info3('Tom', 34, '男') # ('Tom', 34, '男')

# 包裹关键字传递
def user_info4(**kwargs):
    print(kwargs)
user_info4(name='Tom', age=19) # {'name': 'Tom', 'age': 19}