class shape:
    def __init__(self, breadth, length):
        self.b = breadth
        self.l = length
    def area(self):
        area = self.b * self.l
        print(area)
class rect(shape):
    pass
class square(shape):
    pass
print("enter the same value if square else different ")
s = rect(2, 13)
s.area()
s = square(2, 103)
s.area()

