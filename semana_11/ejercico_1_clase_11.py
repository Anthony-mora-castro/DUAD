import math

class circle:
     def __init__(self,radius):
          self.radius = radius

     def get_area(self):
          return math.pi * self.radius ** 2
     
circle_area = circle(5)

print(circle_area.get_area())           
