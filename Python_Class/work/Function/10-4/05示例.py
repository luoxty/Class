user_name = 13321
password = 133211

def login():
    for i in range(0,3):
        name = int(input('请输入账号:'))
        if name == user_name:
            psw = int(input('请输入密码:'))
            if psw == password:
                print('登录成功'.center(40, '='))
                return
            else:
                print('密码错误'.center(40, '='))
                if i == 2:
                    print('您的机会已用完,请12小时之后再试')
                else:
                    print('您还有%s次机会' % (2 - i))
        else:
            print('账号不存在'.center(40, '='))
            if i == 2:
                print('您的机会已用完,请12小时之后再试')
            else:
                print('您还有%s次机会' % (2 - i))
res = login()


def regist():
    while 1:
        print('请注册'.center(40, '='))
        re_name = int(input('请输入账号:'))
        if re_name == user_name:
            print(''.center(40, '='))
        else:
            re_psw = int(input('请输入密码:'))
            return '注册成功'.center(40, '=')
re = regist()
print(re)