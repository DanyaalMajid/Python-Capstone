from abc import ABC, abstractmethod
from math import pi, sqrt

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Diamond(Shape):
    def __init__(self, diagonal1, diagonal2):
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2

    def area(self):
        return (self.diagonal1 * self.diagonal2) / 2

    def perimeter(self):
        return 4 * sqrt((self.diagonal1 / 2) ** 2 + (self.diagonal2 / 2) ** 2)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

def main():
    diamond = Diamond(10, 20)
    print("Diamond area:", diamond.area())
    print("Diamond perimeter:", diamond.perimeter())

    rectangle = Rectangle(10, 20)
    print("Rectangle area:", rectangle.area())
    print("Rectangle perimeter:", rectangle.perimeter())

    circle = Circle(9)
    print("Circle area:", circle.area())
    print("Circle perimeter:", circle.perimeter())

    triangle = Triangle(20, 30, 40)
    print("Triangle area:", triangle.area())
    print("Triangle perimeter:", triangle.perimeter())

if __name__ == "__main__":
    main()
