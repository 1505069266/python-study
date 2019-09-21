# 单例模式  不管创建多少次  都是同一个对象  比如windows的垃圾箱,不管打开几个窗口都是指向的同一个垃圾站

class Dog(object):

    __instance = None

    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:   
            # return object.__new__(cls)
            return cls.__instance


a = Dog()
print(id(a))
b = Dog()
print(id(b))
# 单例的意思是  a和b指向同一个对象