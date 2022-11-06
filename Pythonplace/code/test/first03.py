print ("     我爱      ")
import random
secret =random.randint(1,200)
temp = input ("猜数字：")
guess = int(temp)
while guess != secret:
    temp = input ("猜数字：")
    guess = int(temp)
    if guess ==secret :
        print ("猜对了")
        print ("游戏结束")
    else:
        if guess>secret:
            print("大了")
        else:
            print ("小了")
