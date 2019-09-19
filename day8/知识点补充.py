a = 100

def test(num):
    # 传入a  其实是新建了num
    num+=num
    print("in --test-- num=%d"%num)

test(a)

print("a=%d"%a)

# 两个值交换

a = 4
b = 5

# 1.
c = 0
c = a
a = b
b = c

# 2
a = a+b
b = a-b
a = a-b

# 3.
a,b = b,a