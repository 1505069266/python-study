

# seek(offset,from)   offset:偏移量   from:方向 0:表示文件开头  1:表示当前位置  2:表示文件末尾

f = open("文件系统.py","r",encoding='UTF-8')
f.seek(5,0)
print(f.tell()) # 显示偏移量


f.seek(5,0)


print(f.read())

f.close()