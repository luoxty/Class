#字典
#访问字典
dict = {"Name":"Zara","Age":"7","Class":"first"}
print(dict["Name"])

#修改字典
dict["Name"] = "LiLy"
print(dict)

#删除
del dict["Name"]
print(dict)
dict.clear()
print(dict)
del dict
print(dict)

#作为函数的参数
def fun(dict):
    dict["name"] = "aaa"
    print("inside:",dict)
dict={"name":"xxx","age":30}
print("before",dict)
fun(dict)
print("after",dict)

#作为函数的返回值
def fun():
    dict = {}
    dict["name"] = "aaa"
    dict["age"] = 30
    dict["gender"] = "male"
    return dict
def show():
    keys = dict.keys()
    for key in keys:
        print(key,dict[key])
dict=fun()
print(dict)
show(dict)