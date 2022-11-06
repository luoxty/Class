# 1.请定义一个交通工具(Vehicle)的类为基类，其中有属性:速度 (speed),方法:移动(move())、设置速度
# (setSpeed(int speed)), 定义一个继承类，重写父类的移动和设置速度方法，并定义加速speedUp()、 减速
# speedDown()等。最后调用这些方法。


class Vehicle:
 def __init__(self, speed):
    self.speed = speed

 def setSpeed(self):
     print(("设置当前交通工具的速度为: %s") % self.speed)

 def move(self):
     print(("当前交通工具正在移动，移动速度为: %s") % self.speed)

class Car(Vehicle):
    def __init__(self, speed):
        self.speed = speed
    def setSpeed(self):
        print(("设置当前车辆的速度为: %s") % self.speed)

    def move(self):
        print(("当前车辆正在移动，移动速度为: %s") % self.speed)

    def speedUp(self):
        self.speed = self.speed+10
        print(("当前车辆已加速，移动速度为: %s") % self.speed)

    def speedDown(self):
        self.speed = self.speed-10
        print(("当前车辆已加速减速，移动速度为: %s") % self.speed)


car = Car(10)
car.setSpeed()
car.move()
car.speedUp()
car.speedDown()

