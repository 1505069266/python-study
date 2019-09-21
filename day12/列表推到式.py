

a = []

for i in range(1,71): # range  含头不含尾  第三个参数    风险:要很大的内存  不能用  python2中不会报错,python3会自动提示
    a.append(i)

print(a)

b = [22 for i in range(1,21)]  # 这就是列表循环式

print(b)

c = [i for i in range(1,11) if i%2==0]


d = [i for i in range(3) for j in range(2)]

f = [(i,j) for i in range(3) for j in range(2)]

e = [(i,j,k) for i in range(3) for j in range(2) for k in range(9)]  # 有几种搭配方式


print(d)
print(f)
print(c)
print(e)