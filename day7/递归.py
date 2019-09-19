def test(a):
    if a ==1:
        return a
    result = a * test(a-1)
    return result


print(test(10))

# 递归的问题  无限循环  必须想清楚什么时候结束 