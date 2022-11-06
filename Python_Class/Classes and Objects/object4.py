class Person(object):
    name='Person类name'
    age='Person类的age'
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print('这里是Person类的构造方法')
    def eat(self):
        print('%s 在吃饭(Person类eat方)'%self.name)
    def sleep(self):
     print('%s 在睡觉(Person类sleep方法)'%self.name)
class Teacher(Person):
    name='Teacher类的name'
    def eat(self):
        print('%s 在吃饭(Teacher类eat方法)' %self.name)
test=Teacher('橙子',11)
test.eat()
test.sleep()
print(test.name)
print(Teacher.age)