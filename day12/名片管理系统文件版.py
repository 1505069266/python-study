# 用来储存名片
card_infors = []


def print_menu():
    """完成打印功能菜单"""
    print("=" * 30)
    print(" 名片管理系统 V1.0.0")
    print(" 1. 添加一个新的名片")
    print(" 2. 删除一个名片")
    print(" 3. 修改一个名片")
    print(" 4. 查询一个名片")
    print(" 5. 显示所有名片")
    print(" 6. 保存信息")
    print(" 7. 退出系统")
    print("=" * 30)


def add_new_card_infor():
    """完成一个添加新的名片"""
    new_name = input("请输入你的名字:")
    new_qq = input("请输入你的QQ号:")
    new_weixin = input("请输入你的微信号:")
    new_addr = input("请输入你的住址:")

    # 定义一个新的字典,用来储存一个新的名片
    new_infor = {}
    new_infor['name'] = new_name
    new_infor['qq'] = new_qq
    new_infor['weixin'] = new_weixin
    new_infor['addr'] = new_addr

    # 将一个字典,添加到列表中
    global card_infors
    card_infors.append(new_infor)


def find_card_infor():
    """用来查询一个名片"""
    global card_infors

    find_name = input("请输入你要查找的姓名:")
    find_flag = 0  # 默认表示没用找到
    for name in card_infors:
        if find_name == name['name']:
            print("%s\t%s\t%s\t%s" % (name['name'], name['qq'], name['weixin'], name['addr']))
            find_flag = 1  # 表示找到了
            break

    # 判断是否找到了
    if find_flag == 0:
        print("查无此人")


def show_add_infor():
    """显示所有名片"""
    global card_infors

    print("姓名\t\tQQ\t\t微信\t\t住址")
    for item in card_infors:
        print("%s\t%s\t%s\t%s\t" % (item['name'], item['qq'], item['weixin'], item['addr']))


def save_2_file():
    """把已经添加的信息保存到文件中"""

    global card_infors

    f = open("peoples.data", "w")

    f.write(str(card_infors))

    f.close()


def load_infor():
    global card_infors
    try:
        f = open("peoples.data", 'r')

        card_infors = eval(f.read())

        f.close()
    except Exception:
        pass


def main():
    """完成对整个程序的控制"""
    # 1.打印功能菜单
    print_menu()

    # 将数据文件打开加载数据
    load_infor()

    while True:

        # 2. 获取用户的输入
        num = int(input("请输入操作序号:"))

        # 3 根据用户的数据执行相应的功能
        if num == 1:
            add_new_card_infor()
        elif num == 2:
            pass
        elif num == 3:
            pass
        elif num == 4:
            find_card_infor()
        elif num == 5:
            show_add_infor()
        elif num == 6:
            save_2_file()
        elif num == 7:
            break
        else:
            print("输入有误,请重新输入")


if __name__ == "__main__":
    # 调用主函数
    main()
