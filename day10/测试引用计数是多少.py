import sys

class T:
    pass

t = T()

count = sys.getrefcount(t)  #比实际数量多1   因为他自己也引用了这个对象

print(count) # 2
