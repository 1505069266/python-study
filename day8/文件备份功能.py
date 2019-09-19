f = open("test.py",'r')

content = f.read()

f.close()

a = open("remark.py","w")

a.write(content)

a.close()


