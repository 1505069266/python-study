import os

os.chdir("电视剧") # 改修路径到电视剧下面

print(os.getcwd()) #查看当前的目录路劲

print(os.listdir())


i = 1
while i < 11:
    file_name = "甄嬛传%d.txt"%i
    f = open(file_name,"w")
    f.write(str(i))
    f.close()
    i+=1

