class Dog:
    def __del__(self):
        print("--英雄死了---")

dog1 = Dog()

dog2 = dog1

del dog1 # 不会带调用 __del__ 方法 ,因为这个对象 还有其他的变量引用指向它,即 引用计数不是0
del dog2   # 此时它的指针也被删除   Dog的 __del__ 方法被调用
# 当这个引用没人用的时候就调用方法  __del__
print("=========")

# 如果在程序结束时,有些对象还存在,那么python解释器会自动调用他们的__del__方法来完成清理工作
