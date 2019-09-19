money = int(input("你有多少钱"))

if money > 100 and money < 1000:
    print("穷")
elif money >= 1000 and money < 10000:
    print("小富")
elif money >=10000 and money < 50000:
    print("大富")
else:
    print("土豪")