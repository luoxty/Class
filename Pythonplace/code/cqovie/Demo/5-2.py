#元组
tup = (1,5,6)
week = ("日","一","二","三","四","五","六")
print(week)
w = input("Enter an integer(0~6):")
w = int(w)
if w>0 and w<6:
    print("星期"+week[w])
else:
    print("输入错误")