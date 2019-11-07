# 所谓修改字符串，指的就是通过函数的形式修改字符串的数据

# replace(): 替换
# 语法: 字符串序列.replace(旧子串, 新子串, 替换次数)
# 替换次数可以不写，则代表全部替换
str1 = 'hello world and python and travelclover and you'
print(str1.replace('and', 'or')) # hello world or python or travelclover or you
print(str1.replace('and', 'or', 1)) # hello world or python and travelclover and you

# split(): 按照指定字符分割字符串
# 语法: 字符串序列.split(分割字符, num)
# num表示的是分割字符的次数，即返回数据个数为num + 1个。
list1 = str1.split('and')
print(list1) # ['hello world ', ' python ', ' travelclover ', ' you']
print(str1.split('and', 1)) # ['hello world ', ' python and travelclover and you']

# join(): 用一个字符或子串合并字符串，即是将多个字符串合并为一个新的字符串
# 语法: 字符或子串.join(多字符串组成的序列)
print('aa'.join(list1)) # hello world aa python aa travelclover aa you

# capitalize(): 将字符串第一个字符转换成大写。
# 注意: 该函数转换后，只有首字符大写，其余字符都小写
str2 = 'pythOn'
print(str2.capitalize()) # Python

# title(): 将字符串每个单词首字母转成大写
print(str1.title()) # Hello World And Python And Travelclover And You

# lower(): 将字符串中大写转小写
str3 = 'PythON'
print(str3.lower()) # python

# upper(): 将字符串中小写转大写
print(str3.upper()) # PYTHON

# lstrip(): 删除字符串左侧空白字符
str4 = '  hello  '
print(str4.lstrip()) # 'hello  '

# rstrip(): 删除字符串右侧空白字符
print(str4.rstrip()) # '  hello'

# strip(): 删除字符串两侧的空白字符
print(str4.strip()) # 'hello'

# ljust(): 返回一个原字符串左对齐，并使用指定字符（默认空格）填充至对应长度的新字符串
# 语法: 字符串序列.ljust(长度, 填充字符)
str5 = 'hello'
print(str5.ljust(10, '*')) # hello*****

# rjust(): 返回一个原字符串右对齐，并使用指定字符（默认空格）填充至对应长度的新字符串
# 语法: 字符串序列.rjust(长度, 填充字符)
print(str5.rjust(10, '*')) # *****hello

# center(): 返回一个原字符串居中对齐，并使用指定字符（默认空格）填充至对应长度的新字符串
# 语法: 字符串序列.just(长度, 填充字符)
print(str5.center(10, '*')) # **hello***