#异常语句1
s="hello"
try:
     int(s)
except Exception as e:
    print(e)

#异常语句2
 # try:
 #     [语句块]
 # except Exception [as reason]:
 #     出现异常(exception)后处理代码
 # finally:
 #     无论如何都会被执行的代码
#异常案例
try:
    s=3+"5"
except Exception as e:
    print(e)
finally:
    print("程序结束运行")

#无异常案例
try:
    s=3+5
except Exception as e:
    print(e)
finally:
    print("程序结束运行")