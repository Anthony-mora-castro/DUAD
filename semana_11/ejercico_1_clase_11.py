class circle():
    def radius(self, r):
        self.r = r
    def get_area(self):
        return 3.1416 * self.r ** 2

circle_area = circle()
circle_area.radius(5)
print(circle_area.get_area())

