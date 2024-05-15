class Triangle:
    def __init__(self, a=3, b=4, c=5):
        self.a = a
        self.b = b
        self.c = c

    def checkIfRight(self, a, b, c):
        if a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == c ** 2 + b ** 2:
            return True
        return False

    def sidesToTuple(self):
        result = (self.a, self.b, self.c)
        return result

    def output(self):
        print(f"Sides of triangle: {self.a}, {self.b}, {self.c}")

triangle = Triangle(1, 2, 3)

triangle.output()
print(triangle.sidesToTuple())



