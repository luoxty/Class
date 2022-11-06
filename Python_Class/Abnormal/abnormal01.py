try:
    name = input("请输入名字")
    print('hello %s' %name)
    print(10/0)

#
except Exception as e:
    print("发现异常:除数不能为0" ,e)
finally:
    print("程序执行完毕")