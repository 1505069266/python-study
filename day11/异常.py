# 异常处理
try:
    11/0
    open("xxx.txt")
    print(num)
    print('顶顶顶')
except (NameError,FileNotFoundError):  #捕获多个异常  放到一个元组中去
    print("出错了 我不知道什么错")
except FileNotFoundError: # 捕获单个异常
    print('dsdwewqewqe')
except Exception as ret:
    print("如果用了Exception,那么意味着只要上面的except没有捕获到异常,这个except一定会捕获到")
    print(ret)
else:
    print('没有异常会执行这里')
finally:
    print("不管有没有异常都会执行的内容")
print("ddddd")