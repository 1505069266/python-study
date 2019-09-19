# 调用函数时,缺省的函数如果没有传入,则被认为是默认值,下例会默认打印的age,如果没有age传入
def main(name,age = 18):
    # 打印任何传入的字符串
    print("name=%s"%name)
    print("age=%d"%age)

main("朱晓乐")
main("郑璇",24)