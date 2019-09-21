

a = (11,22,33,44,55,66) # 元组

b = [44,55,66,77,88,99] # 列表

c = {11,22,33,11,22,55} # 集合

print(type(a))
print(type(b))
print(type(c))
print(c)

# 去重方法
aa = [11,222,222,11,21,22,3231,11,3123,44,44,223,222,434,6565,23]

bb = []

# for i in aa:
#     if i not in bb:
#         bb.append(i)

print(bb)

# 将一个列表转化成集合

f = set(aa)

bb = list(f)


print(bb)