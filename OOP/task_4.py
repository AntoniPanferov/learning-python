class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

a = Rectangle(2, 1)
b = Rectangle(1, 2)
print(a.area == b.area)
print(f'{a.length} {b.length}')
print(f'{a.length} {b.area}')
