str1=[]
x=1
while(x>0):
    a=int(input('请选择你要进行的操作0——5（退出，增加，修改，删除，查询，显示）：'))
    if a==1:
        str = {}
        for i in range(4):
            if i == 0:
                i = input('请输入学生姓名:')
                str['姓名']=i
            if i == 1:
                i = input('请输入学生学号:')
                str['学号']=i
            if i == 2:
                i = input('请输入学生年龄:')
                str['年龄']=i
            if i == 3:
                i = input('请输入学生手机号:')
                str['手机号']=i
        str1.append(str)
        print("已成功增加！")

    if a==2:
        v=input("请输入你想要更改学生的学号：")
        for i in range(len(str1)):
            if v in str1[i].values():
                str2=str1[i]
                for k in range(len(str1[i])):
                    if k == 0:
                        a = input('请输入新的学生姓名:')
                        str2['姓名']=a
                    if k == 1:
                        a = input('请输入新的学生学号:')
                        str2['学号']=a
                    if k == 2:
                        a = input('请输入新的学生年龄:')
                        str2['年龄']=a
                    if k == 3:
                        a = input('请输入新的学生手机号:')
                        str2['手机号']=a
        print("已成功修改")
    if a == 3:
        v = input("请输入你想要删除学生的学号：")
        for i in range(len(str1)):
            if v in str1[i].values():
                del str1[i]
        print("已成功删除")
    if a == 4:
        v = input("请输入你想要查询学生的学号：")
        for i in range(len(str1)):
            if v in str1[i].values():
                print('查询到信息：',str1[i])
    if a==5:
        print('所有学生信息：')
        for i in str1:
            print(i)