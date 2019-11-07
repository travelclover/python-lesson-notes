# isalpha(): 如果字符串至少有一个字符并且所有字符都是字母则返回True，否则返回False。
str1 = 'hello'
str2 = 'hello123'
print(str1.isalpha()) # True
print(str2.isalpha()) # False

# isdigit(): 如果字符串只包含数字则返回True，否则返回False。
str3 = '123'
str4 = 'as123'
str5 = '11.23'
print(str3.isdigit()) # True
print(str4.isdigit()) # False
print(str5.isdigit()) # False

# isalnum(): 如果字符串至少有一个字符并且所有字符都是字母或数字则返回True，否则返回False。
str6 = 'asd123'
str7 = '123-'
print(str6.isalnum()) # True
print(str7.isalnum()) # False

# isspace(): 如果字符串只包含空白，则返回True，否则返回False。
str8 = '1 1 1 1'
str9 = '  '
print(str8.isspace()) # False
print(str9.isspace()) # True