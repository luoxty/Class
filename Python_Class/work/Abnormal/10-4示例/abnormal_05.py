zhlist = []
mmlist = []
def zhuce():
    try:
        x = input("输入注册的账号")
        y = input("输入注册的密码")
        if len(x) > 0 and len(y) > 0:
            zhlist.append(x)
            mmlist.append(y)
        else:
            raise Exception("输入的账号或密码不能为空")
    except Exception as err:
        print(err)

def denglu():
    try:
        for i in range(3):
            x = input("输入登录账号")
            y = input("输入对应的密码")
            if len(x) > 0 and len(y) > 0:
                if x in zhlist and y in mmlist:
                    print("登录成功")
                    break
                else:
                    print("账号或密码错误，登录失败")
            else:
                print("输入的账号或密码不能为空")
            if i == 3:
                raise Exception("登录次数用完,登录失败")
    except Exception as err:
        print(err)
zhuce()
denglu()