# 将一个对象转化成整数类型  int(对象)
age = "20"

print(type(age))

if int(age) > 18:
    print("已经成年  可以去网吧")
    print("已经成年  可以去嫖娼")
else:
    print("未成年人禁止上网")

name = "朱晓乐"
zhu_age = 23
zhu_height = "170cm"

print("我叫%s,我今年%d岁了,身高%s" % (name, zhu_age, zhu_height))
