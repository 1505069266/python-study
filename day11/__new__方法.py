class Dog(object):
    def __init__(self):
        print("__init__")

    def __del__(self):
        print("__del__")

    def __str__(self):
        print("__str__")

    def __new__(cls): # cls此时是Dog指向的那个类对象
        print(id(cls))
        return object.__new__(cls)
        print("__new__")

print(id(Dog))
xtq = Dog()  # 做了三件事情   1.变量 = 调用__new__方法来创建对象 ,然后找一个变量来接收__new__的返回值,这个返回值表示创建出来的对象的引用
#                          2.__init__(刚刚创建出来的对象的引用)
#                         3. 返回对象的引用
