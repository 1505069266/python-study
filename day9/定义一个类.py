# 类要用大驼峰写法

class Cat:
    # 属性



    # 方法
    def eat(self):
        print("猫在吃鱼..")
    
    def drink(self):
        print("猫在喝水..")

    def introduce(self):
        print("%s的年龄是:%d"%(self.name,self.age))

# 创建一个新的对象  返回对象的引用
tom = Cat()

tom.eat()

tom.name = "汤姆"

tom.age = 18
tom.introduce()  # tom.introduce(tom)
# 获取对象的属性

lanmao = Cat()

lanmao.name = "蓝猫"
lanmao.age = 10
lanmao.introduce() # tom.introduce(lanmao)