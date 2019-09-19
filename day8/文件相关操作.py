import os

os.rename("文件系统.py","文件.py") # 给文件重命名

# 删除文件
os.remove("test.py")

# 创建文件夹

os.mkdir("我是被python创建的")

# 获取当前目录
os.getcwd()


# 改变目录
os.chdir("day8")

# 获取目录列表

os.listdir("../")


# 删除文件夹
os.rmdir("文件夹名字")
