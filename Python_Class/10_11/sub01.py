import re  # 导入正则表达式库
name = input("请输入用户名，以字母开头，长度不少于3位，只能包含字母、数字、下划线:")  # 提示用户输入
match = re.match(r"^[a-zA-Z]\w{2,}$", name)  # 验证输入是否符合要求
while match is None:  # 如果不符合要求，则循环
    print("用户名不符合要求，请重新输入：", end=" ")  # 提示用户名不符合要求
    name = input()  # 重新获取用户输入
    match = re.match(r"^[a-zA-Z]\w{2,}$", name)  # 验证输入是否符合要求
    print("恭喜你， {} ，注册成功!".format(name))  # 提示注册成功