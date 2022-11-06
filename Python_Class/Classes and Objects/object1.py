class ComplexNumber:
    def __init__(self, r = 0, i = 0):
        """"初始化方法"""
        self.real = r
        self.r=r
        self.imag = i
        self.i=i

    def getData(self):
        print("{0}+{1}j".format(self.real, self.imag))
c = ComplexNumber(5, 6)
c.getData()