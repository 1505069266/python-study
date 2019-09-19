class Dog(object):
    def print_self(self):
        print("大家好,我说xxxx,希望大家多多关照")

class xiaotq(Dog):
    def print_self(self):
        print("hello everybody,我是你们的老大")

def introduce(temp): # 定义的时候不知道对象是谁  运行的时候才知道   
    temp.print_self()

dog1 = Dog()

dog2 = xiaotq()

introduce(dog1)

introduce(dog2)

#  python的传值都是传引用,指向的都是同一个对象

