import re

while 1 :
    start = input("选择正则表达式:")
    if(start == '1'):
        while 1:
            l1 = input("1.输入数字:")
            if (l1 == "q"):
                print("退出正则表达式1")
                break
            else:
                ret = re.match(r'(50|[1-4]\d|[1-9])$', l1)
                print(ret.group())
    if(start == '2'):
        while 1:
            l2 = input("2.输入QQ号:")
            if (l2 == "q"):
                print("退出正则表达式2")
                break
            else:
                pattern = "^[1-9][0-9]{4,9}$"
                result = re.match(pattern, l2)
                if result:
                    print("%s是有效QQ号。" % result.group())
                else:
                    print("%s是无效QQ号。" % l2)
    if(start =='3'):
        while 1:
            l3 = input("3.输入字符串:")
            if (l3 == "q"):
                print("退出正则表达式3")
                break
            else:
                ret3 = re.sub(r'\d{5,}', '$', l3)
                print(ret3)

    if(start =='4'):
        while 1:
            l4 = input("4.输入字符串")
            if (l4 == "q"):
                print("退出正则表达式4")
                break
            else:
                ret4 = re.findall(r'[a-zA-Z]', l4)
                print(ret4)
    if(start == '5'):
        while 1:
            l5 = input("5.输入字符串:")
            if (l5 == "q"):
                print("退出正则表达式5")
                break
            else:
                ret5 = re.sub(r'([a-zA-Z])\1+ ', r'\1', l5)
                print(ret5)
    if(start =='6'):
        while 1:
            l6 = input("6.输入字符串:")
            if (l6 == "q"):
                print("退出正则表达式6")
                break
            else:
                ret6 = re.findall(r'\b\w{3}\b', l6)
                print(ret6)
    if(start =='7'):
        while 1:
            l7 = input("7.输入字符串:")
            if (l7 == "q"):
                print("退出正则表达式7")
                break
            else:
                ret7 = re.findall(r'\b\w{3}\b', l7)
                print(ret7)

    if (start == "q"):
        print("退出")
        break
