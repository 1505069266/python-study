# 1.提示并获取用户输入
player = int(input("请输入 0剪刀 1石头 2布:"))
import random

computer = random.randint(0, 2)
# 2.判断用户的输入,然后显示对应的结果

if (player == 0 and coumpter == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
    print("你赢了")
elif player == computer:
    print("平局")
else:
    print("你输了")
