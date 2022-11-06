class Student:
    def __init__(self, name,age,score):
        """"初始化方法"""
        self.name = name
        self.age = age
        self.score= score
    def get_name(self):
        return str(self.name)
    def get_age(self):
        return str(self.age)
    def get_course(self):
        return int(max(self.score))
c = Student('董+i',55,(50,60,70))
print(c.get_name())
print(c.get_age())
print(c.get_course())
