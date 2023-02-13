class Points:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f'({self.x},{self.y})')

    def move(self, x1, y1):
        self.x += x1
        self.y += y1

    def dist(self, x2, y2):
        print(f'({abs(self.x - x2)},{abs(self.y - y2)})')


m = Points(1, 1)
m.show()
m.move(1, 2)
m.show()
m.dist(2, 3)