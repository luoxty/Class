# 5.将AniamI作为父类，定义两个动物作为派生类，派生类定义属于该类动物的特有属性和方法。
class AniamI:
    def __init__(self,weight):
        self.weight = weight
    def eat(self):
        print("吃东西")
