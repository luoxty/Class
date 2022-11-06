#列表添加元素
list = ["history","english","math",1999,2019]
list2 = [1,2,"ab"]
list.append(list2[2])
print(list)
list.extend(list2)
print(list)
list.insert(1,list2[2])
print(list)
list3 = list + list2
print(list3)
