class Animal:
    def eat(self):
        print('eat')

    def drink(self):
        print("drink")

    def sleep(self):
        print('sleep')

    def run(self):
        print("running")

class Dog(Animal): # 继承Animal的方法的方法
    def bark(self):
        print("汪汪汪")

class Cat(Animal):
    def bark(self):
        print("喵喵喵")

class Xtianq(Dog):
    def fly(self):
        print("飞")

    def bark(self):
        print("狂叫")
        # 调用父类方法
        Dog.bark(self)

        # 调用父类方法
        super().bark()

xiaotianq = Xtianq()

xiaotianq.bark()

xiaotianq.eat()