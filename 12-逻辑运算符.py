# 逻辑运算符
# and   布尔“与”
# or    布尔“或”
# not   布尔“非”

a = 1
b = 2
c = 3

print((a < b) and (a < c)) # True
print((a < b) and (a > c)) # False

print((a < b) or (a > c)) # True

print(not (a > b)) # True
