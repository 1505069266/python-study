names = ["老王","老刘","老郑","老李","老朱","老明"]
# 逆序
print(names[::-1])

# 增删改查
names.append("朱晓乐")
names.insert(3,"郑玄")
names2 = ["葫芦娃","叮当猫","悟空"]
names3 = names + names2
print(names)
# names3.extend(names2)
# print(names3)


names.pop()

print(names)

names.remove("老王")

print(names)

del names[2]

print(names)

names.append('2')
names.append("2")
names.append("2")

print(names)
if "朱晓乐" in names:
    print("找到了")

if "朱晓乐" not in names:
    print("可以添加朱晓乐")


