fo = open("/Python_Class\\File Operation\\1.txt", "r+")
try:
    with open("1.txt",mode='r') as ff:
        print("文件存在")
        print(ff.readlines())
except FileExistsError:
    with open ("1.txt",mode='w+',encoding='utf-8') as ff:
        print("文件创建成功")
        ff.write("dic")
        ff.seek(0)
        print(ff.read())



