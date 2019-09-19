import os

# 1.获取一个要重命名的文件夹的名字
folder_name = input("请输入要重命名的文件夹:")
#  输入的路径是相对路径  需要注意
# 2.获取那个文件夹中所有的文件名字
file_names = os.listdir(folder_name)

os.chdir(folder_name)
# 3.对获取的名字进行重命名即可

for name in file_names:
    print(name)
    os.rename(name,"[乐乐出品]" + name)
