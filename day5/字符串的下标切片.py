name = "abcdefghijkmlnopqrstuvwxyz"

print(len(name))
print(name[2])
print(name[1])
print(name[0])
print(name[-1])

print(name[0:-1])  # 含头不含尾

print(name[2:])  # 空一个表示到尾部  或者头部

print(name[2::2])  # 空一个取值
# [起始位置:终极位置:步长]]

# 逆序
print(name[-1::-1])
# 正序输出
print(name[::1])
