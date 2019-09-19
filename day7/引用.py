a = 100
b = a
#  两者指向同一个值100

print(b) # 100 因为b指向的是100的值

print(id(a)) 
print(id(b))

print(id(b) == id(a)) # 返回True

A = [11,22,33]
A.append(222)
B = A #将A的指向给了B  两者指向一个
print(id(A)) 
print(id(B))

# 注意点  python自动清除垃圾


