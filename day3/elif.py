money = int(input("你有多少钱"))

if 100 < money < 1000:
    print("穷")
elif 1000 <= money < 10000:
    print("小富")
elif 10000 <= money < 50000:
    print("大富")
else:
    print("土豪")
