info = {
    "name":"朱晓乐",
    "age":23,
    "gender":99
}

info["QQ"] = 1505069266

print(info)

print(info.get("QQ"))
del info["QQ"]

print(info)