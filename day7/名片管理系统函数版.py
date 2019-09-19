# 用来储存名片
lists = []

# 1.打印功能提示
def print_menu():
    print("="*30)
    print(" 名片管理系统 V1.0.0")
    print(" 1. 添加一个新的名片")
    print(" 2. 删除一个名片")
    print(" 3. 修改一个名片")
    print(" 4. 查询一个名片")
    print(" 5. 退出系统")
    print("="*30)

def add_new_card():
    """这是用来增加名片功能的方法"""
    new_name = input("请输入新的名字:")
    new_weixin = input("请输入新的QQ:")
    new_qq = input("请输入新的微信:")
    new_addr = input("请输入新的住址:")

    # 定义一个新的字典
    new_info = {}
    new_info["name"] = new_name
    new_info["weixin"] = new_weixin
    new_info["qq"] = new_qq
    new_info["addr"] = new_addr
    global lists
    lists.append(new_info)
    print(lists)
help(add_new_card)
print_menu()
# 2.获取用户的输入


# 3.根据用户的数据执行相应的功能

while True:
    num = int(input("请输入操作序号:"))
    if num == 1:
        add_new_card()
    elif num == 2:
        pass
    elif num == 3:
        pass
    elif num == 4:
        find_name = input("请输入要查找的姓名:")
        find_flag = 0
        for temp in list:
            if find_name == temp["name"]:
                print("%s\t%s\t%s\t%s"%(temp["name"],temp["qq"],temp["weixin"],temp["addr"]))
                find_flag = 1 #表示找到了
                break #跳出循环
        if find_flag == 0:
            print("查无此人")
        pass
    elif num == 5:
        print("姓名\t\tQQ\t\t微信\t\t住址")
        for temp in list:
            print("%s\t%s\t%s\t%s"%(temp["name"],temp["qq"],temp["weixin"],temp["addr"]))
    elif num == 6:
        break
    else:
        print("输入有误,请重新输入")

