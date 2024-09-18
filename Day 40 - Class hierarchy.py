"""
Day 40 - Class hierarchy
Create a class hierarchy for different shapes (circle, square, triangle).
"""

class Shape:
    def __init__(self, name) -> None:
        self.name = name

class Circle(Shape):
    def __init__(self, radius) -> None:
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        print (f"The {self.name} has an area of {3.14159 * self.radius ** 2}")

class Square(Shape):
    def __init__(self, side) -> None:
        super().__init__("Square")
        self.side = side

    def area(self):
        print (f"The {self.name} has an area of {self.side * self.side}")

class Rectangle(Shape):
    def __init__(self, side1, side2) -> None:
        super().__init__("Square")
        self.side1 = side1
        self.side2 = side2

    def area(self):
        print (f"The {self.name} has an area of {self.side1 * self.side2}")

c = Circle(3)
s = Square(4)
r = Rectangle(2,3)
c.area()
s.area()
r.area()

Circle(6).area()