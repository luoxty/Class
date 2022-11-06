# 3.定义一个圆类-
# Circle, 在类的内部提供一-个属性:半径@，同时提供两个方法:
# 计算面积
# ( getArea() )和计算周长(getPer imeter())。通过两个 方法计算圆的周长和面积并且对计算结果进行
# 输出。最后调用这些方法。
class Circular:
    radius = 0
    def __init__(self,radius):
        self.radius=radius

    def getArea(self):
        s = self.radius * self.radius * 3
        print(s)
    def getPer(self):
        l = self.radius * 3 * 2
        print(l)

c = Circular(10)

c.getArea()
c.getPer()