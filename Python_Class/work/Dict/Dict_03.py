person = {'name': ['黎明','杨柳','张一帆','许可','王笑笑','陈欣',], 'sex':['男','女','男','女','女','女'], 'age': [19,18,18,20,19,19]}
list1 = person['sex']
print(list1.count("男"))
print(list1.count("女"))
list2 = person['age']
list3 = person['name']
for i in range(len(list2)):
    if(list2[i] > 18):
        print(list3[i])


