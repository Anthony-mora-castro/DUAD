from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius
    
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius
    
    def calculate_area(self):
        return math.pi * self.radius ** 2

class Square(Shape):

    def __init__(self, size):
        self.size = size

    def calculate_perimeter(self):
        return self.size * 4
    
    def calculate_area(self):
        return self.size ** 2 
    
class Rectangle(Shape):
    
    def __init__(self,length, width):
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        return (self.length + self.width) * 2
    
    def calculate_area(self):
        return self.length * self.width


circle = Circle(radius = 5)
print(f'The perimeter of the circle is: {circle.calculate_perimeter()} and the area is: {circle.calculate_area()}')

square = Square(size = 2)
print(f'The perimeter of the square is: {square.calculate_perimeter()} and the areas is: {square.calculate_area()}')

rectangle = Rectangle(length = 4, width = 4)
print(f'The perimeter of the rectangle is: {rectangle.calculate_perimeter()} and the area is: {rectangle.calculate_area()}')

