class Tool(object): # 类对象
    # 类属性
    num = 0  # 类属性  共同拥有一个类属性  在实例对象中共享这个类属性

    # 方法
    def __init__(self,new_name):
        # 实例属性
        self.name = new_name
        # 对类属性=+1
        Tool.num += 1 # 这里的类属性是  Tool.num   不是self.num

# 实例属性: 和具体的某个实例对象有关系,并且一个实例对象和另一个实例对象是不共享属性的

# 类属性: 类属性所属于类对象,并且多个实例对象之间,共享同一个属性

tool1 = Tool("铁锹") # 实例对象
tool2 = Tool("工兵铲") # 实例对象
tool3 = Tool("水桶") # 实例对象

print(tool3.num)