

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f'Point({self.x}, {self.y})'

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)


p1 = Point(10,4)
p2 = Point(5,4)
print(p1==p2)
print(p1 - p2)
print(p1 * p2)
