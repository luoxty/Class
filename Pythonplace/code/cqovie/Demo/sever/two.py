#对象的初始化
class Student:
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age
    def show(self):
        print(self.name,self.gender,self.age)
s=Student("Tom","male",19)
s.show()
#对象的初始化
class Student:
    def __init__(self,name="",gender="",age=""):
        self.name=name
        self.gender=gender
        self.age=age
    def show(self):
        print(self.name,self.gender,self.age)
s1=Student("Tom","male",19)
s1=Student("Tom","famle")
s3=Student("Tom")

