class Game(object):
    # 类属性
    num = 0

    # 实例方法 写self 参数是self 是实例的本体
    def  __init__(self,new_name):
        # 实例属性
        self.name = new_name

    # 类方法 写 cls表示自己的类  参数是cls  也就是类本体
    @classmethod  
    def add_num(cls):
        cls.num = 100

    #静态方法  没有参数
    @staticmethod
    def print_nenu():
        print("-----------")
        print("  穿越火线V1.1")
        print("1,开始游戏")
        print("2.结束游戏")
        print("-----------")

game = Game("游戏")
  
Game.add_num() #调用类方法  可以通过类的名字调用类方法

game.add_num() #  调用类方法 还可以通过这个类创建出来的对象,去调用这个类方法

print(Game.num)


Game.print_nenu() # 调用静态方法

game.print_nenu()# 调用静态方法