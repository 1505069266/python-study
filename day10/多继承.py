# 一个子类继承  多个类的属性和方法

class Base(object):# 默认继承object  不写就是继承object
    def test(self):
        print("test1")

class Aase(object):# 默认继承object  不写就是继承object
    def testA(self):
        print("test1A")


class A(Aase):
    def test1(self):
        print("test11")

class B(Base):
    def test2(self):
        print("test2")

class C(A,B): #继承A和B的属性和方法
    def test3(self):
        print("test3")

c = C()

c.test1()
c.test2()
c.test3()
c.testA()
c.test()