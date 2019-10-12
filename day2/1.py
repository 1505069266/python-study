# 当行注释
# print("dddd第三代")


# 多行注释
"""
print("点点点")
"""

# 变量
applePrice = 7  # 苹果7元一斤
weight = 3.5  # 每斤苹果3.5元

money = applePrice * weight  # 算出总价

money = money - 10  # 打折活动减价

print(money)

height = 170
name = "朱晓乐"

print("你的身高是:%d" % height)
# 拼接数字的时候  %d表示拼接数字


print("你的身高是:%s" % name)
# 拼接字符串的时候  %s表示拼接字符串


# 1. 使用input获取必要的信息

# 2. 使用print输出信息

yourName = input("请输入你的名字")

yourAge = input("请输入你的年龄")

yourheight = input("请输入你的身高")

youruniversity = input("请输入你的大学")

print("姓名:%s" % yourName)

print("年龄:%s" % yourAge)

print("身高:%s" % yourheight)

print("毕业院校:%s" % youruniversity)
