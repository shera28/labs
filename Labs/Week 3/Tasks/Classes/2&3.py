class Shape:
    ar = 0
    def area(self):
        print(self.ar)


class Square(Shape):
    def __init__(self, length):
        self.legth = length
    def area(self):
        print(self.legth ** 2)


class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def area(self):
        print(self.width * self.height)


sh = Shape()
sh.area()
sq = Square(5)
sq.area()
rec = Rectangle(4, 5)
rec.area()