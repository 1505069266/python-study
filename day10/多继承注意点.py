# 一个子类继承  多个类的属性和方法

class Base(object):# 默认继承object  不写就是继承object
    def test(self):
        print("Ba")

class Aase(object):# 默认继承object  不写就是继承object
    def test(self):
        print("Aa")


class A(Aase):
    def test(self):
        print("A")

class B(Base):
    def test(self):
        print("B")

class C(A,B): #继承A和B的属性和方法
    def test(self):
        print("C")

c = C()

c.test()
# 写代码的时候尽可能的不要写重复的方法名
print(C.__mro__)  # 如果方法的名字都相同的时候,谁先执行,根据这个方法中的方法的排序来决定方法的执行先后