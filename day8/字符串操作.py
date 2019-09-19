a = "hello world and hahha or haha"

print(a.find('haha'))

print(a.find('hahaq'))


print(a.index('haha'))

print(a.count("h"))

print(a.replace("h","H"))

print(a.replace("h","H",2))

print(a.split(" "))

print(a.title())

print(a.startswith("h"))

print(a.endswith(".txt")) # 判断是不是以.txt结尾的文件


print(a.upper())

print(a.lower())

print(a.ljust(100))  # 做对齐


print(a.rjust(100)) # 右对齐
 

print(a.center(100)) # 居中对齐

print(a.lstrip()) # 去除左边空格

print(a.rstrip()) # 去除右边空格

print(a.strip()) # 去除两边的空格

print(a.partition("and"))

print(a.rpartition("and"))

print(a.splitlines()) # 换行切割

print(a.isalpha())

print(a.isdigit())

print(a.isalnum())

