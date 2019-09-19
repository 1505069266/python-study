def test(*args,**kwargs):
    print(args)
    print(kwargs)


A = (22,33,33,1,2,33,12312,21321)
B = {"name":"zhuxiaole","age":18}

test(A,B)


# 传递元组*参数   传递字典**参数
test(*A,**B)