# 不确定几个参数
# *args表示不确定几个参数,必须放在参数的末尾
def sum(*args):
    result = 0
    for num in args:
        result+=num
    print(args)

    return result
    print(result)

print(sum(20,20,20,20,20))

#  单个元组 加逗号    (1,)


#  带变量名的参数用**kwagrs接收
def test(*args,**kwargs):
    print(kwargs)
    print(args)


test(1,2,3,4,a=222,b=222)

