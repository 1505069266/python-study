# 类要用大驼峰写法

class Cat:
    """定义了一个类"""
    # 属性
    # 初始化对象
    def __init__(self,new_name,new_age):# 这个方法自动执行  除了self的参数是需要创建对象的时候输入的参数
        self.name = new_name
        self.age = new_age

    def __str__(self): #打印对象的返回信息就这个函数返回的信息
        return "名字:%s,年龄:%d"%(self.name,self.age)

    # 方法
    def eat(self):
        print("猫在吃鱼..")
    
    def drink(self):
        print("猫在喝水..")

    def introduce(self):
        print("%s的年龄是:%d"%(self.name,self.age))

# 创建一个新的对象  返回对象的引用
tom = Cat("tom",40)
tom.introduce()  # tom.introduce(tom)
# 获取对象的属性

lanmao = Cat("lanmao",10)

lanmao.name = "蓝猫"
lanmao.age = 10
lanmao.introduce() # tom.introduce(lanmao)

print(tom)  #打印的是类的 def __str__方法的return
print(lanmao)  #打印的是类的 def __str__方法的return
# 创建对象的过程:
#   1.创建一个对象
#   2.python会自动的调用__init__方法
#   3.返回这个对象的引用