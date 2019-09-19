# 1.获取要复制的文件名
old_file_name = input("亲输入要复制的文件名(需要后缀):")



# 2.打开要复制的文件
f_read = open(old_file_name,"r")

# 3.创建一个新的文件
position = old_file_name.rfind(".")
new_file_name = old_file_name[0:position] + "[复件]" + old_file_name[position:]
f_wirte = open(new_file_name,"a")


# 4.从old文件中,读取数据,写入到new文件中
while True:
    content = f_read.read(1024)

    if len(content) == 0:
        break
    f_wirte.write(content)

# 5.关闭两个文件

f_read.close()
f_wirte.close()