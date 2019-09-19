# def 函数名:
#     dosomething.....

# 匿名函数
# lambda 参数:式子
# 定义匿名函数
# 自带return
func = lambda x,y:x+y
print(func(1,3))


infors = [{"name":"zhuxiaole","age":18},{"name":"zhengxuan","age":15}]

infors.sort(key=lambda x:x["name"])

print(infors)

infors.sort(key=lambda x:x["age"])
print(infors)

print(110300+9670+6000+2000)