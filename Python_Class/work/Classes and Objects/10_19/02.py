# 2.编写程序用于显示 人的姓名和年龄。定义一个人类Person。该类中应该有两个私有属性: 姓名(nan
# 和年龄(age)
# , 定义构造方法用来初始化数据成员。再定义显示(display()) 方法将姓名和年龄打印出来
# 调用方法然后将信息显示。
class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    def display(self):
        print("姓名：: %s  年龄 %d 。" %(self.__name,self.__age))

p = Person('dong',10)
p.display()