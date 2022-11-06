class Ticket:
    def __init__(self, weekend=False, child=False):
        self.exp = 100
        if weekend:
            self.inc = 1.2
        else:
            self.inc = 1
        if child:
            self.discount = 0.5
        else:
            self.discount = 1
    def calcPrince(self, num):
        P = self.exp * self.inc * self.discount * num
        return P
w =str(input("请输入是周末还是周内:"))
if(w == "周末"):
    w = weekwnd=True
else:
    w = weekwnd=False
a = int(input("请输入大人人数"))
c = int(input("请输入小孩人数"))
adult = Ticket(w)
child = Ticket(child=True)
print( a+"个成人+"+c+"一个小孩平日票价为：%.2f" % (adult.calcPrince(a) + child.calcPrince(c)))