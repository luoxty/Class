#继承
#父类
class Student:
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age
    def show(self,end='\n'):
        print(self.name,self.gender,self.age)
#子类
class Graduate(Student):
    def __init__(self,name,gender,age,dept,major,address,time):
        Student.__init__(self,name,gender,age)
        self.major=major
        self.address=address
        self.time=time
    def show(self):
        Student.show(self,'')
        print(self.major,self.time,self.address)