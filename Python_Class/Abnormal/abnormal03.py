while True:
    try:
        x = int(input("请输入一个数字: "))
        y = input("请输入/: ")
        if (y != '/'):
            raise Exception('您输入的不是/，请重新输入！')
        print('3/x=', 3 / x)
        break
    except ValueError:
        print("您输入的不是数字，请再次尝试输入！")
    except ZeroDivisionError:
        print('您输入的是0，请重新输入！')
    except BaseException as e:
        print('出错了,', e)
