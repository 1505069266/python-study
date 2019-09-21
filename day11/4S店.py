class CarStore(object):
    def __init__(self):
        self.factory = Factory()

    def order(self,money,car_type):
        # if money > 50000:
        #     return Car()  #这个Car() 表示Car() 的实例对象
        return self.factory.select_car_type(car_type)

class Factory(object):
    def select_car_type(car_type):
        if car_type == "Audi":
            return Audi()
        elif car_type == "Car":
            return Car()
        else:
            return BMW()


class Car(object):
    def move(self):
        print("car moving")

    def music(self):
        print("car musicing")
    
    def stop(self):
        print("car stopping")

class Audi(object):
    def move(self):
        print("Audi car moving")

    def music(self):
        print("Audi car musicing")
    
    def stop(self):
        print("Audi car stopping")

class BMW(object):
    def move(self):
        print("BMW car moving")

    def music(self):
        print("BMW car musicing")
    
    def stop(self):
        print("BMW car stopping")

car_store = CarStore()

car1 = Car()

car = car_store.order(1000000,"Audi")

car.move()

car.music()

car.stop()

# 开发文档
# def select_car_type(car_type)
# 功能: 返回一个汽车对象的引用
# 参数: 需要得到汽车的类型

# 设计模式
# 简单工厂模式
# 
