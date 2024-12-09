from abc import ABC, abstractmethod

# Abstract Class
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

# Rectangle Class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

# Circle Class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14159 * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * 3.14159 * self.radius

# Test the classes
if __name__ == "__main__":
    # Rectangle Example
    rect = Rectangle(length=5, width=3)
    print("Rectangle Area:", rect.calculate_area())
    print("Rectangle Perimeter:", rect.calculate_perimeter())

    # Circle Example
    circle = Circle(radius=4)
    print("Circle Area:", circle.calculate_area())
    print("Circle Perimeter:", circle.calculate_perimeter())
