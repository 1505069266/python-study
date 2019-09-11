
motorcycles = ['朱晓乐','郑璇','张晓媛']

print(motorcycles)

motorcycles[0] = "朱晓飞"

print(motorcycles[-2])

#添加一个到尾部
motorcycles.append("章小环")

print(motorcycles)

#插入一个到指定位置
motorcycles.insert(1,"郑楚凡")

print(motorcycles)

#删除一个或多个元素  直接del  加那个元素

del motorcycles[-1]
print(motorcycles)

# pop()也是删除一个,不过是默认删除最后一个元素,如果往里面填索引,就是删除指定的元素了
pop_motorcycles = motorcycles.pop()
pop_index_motorcycles = motorcycles.pop(1)
print(pop_motorcycles)
print(pop_index_motorcycles)


# 删除你不知道位置的指定的值,不是索引       remove(值)  只能删除第一个,如果数组中有很多个,需要循环数组来删除所有的相同值
motorcycles.remove('郑璇')
print(motorcycles)

