
class ShortInputException(Exception):
    """自定义的异常"""
    def __init__(self,length,atleaet):
        # super().__init__()
        self.length = length
        self.atleast = atleast

def main():
    try:
        s = input("请输入:")
        if len(s) < 3:
            # raise引发一个你定义的异常
            raise ShortInputException(len(s),3)
    except ShortInputException as result: # 这个变量被绑定到了错误的实例
        print("ShortInputException:输入的长度是%d,长度最少应是%d"%(result.length, result.atleaet))
    else:
        print("没有异常发生")