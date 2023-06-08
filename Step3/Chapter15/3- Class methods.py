# Write a class method similar to total_area() that returns the total circumference of
# all circles.

"""circle_cm module: contains the Circle class."""
class Circle:
    """Circle class"""
    all_circles = [] 
    pi = 3.14159
    def __init__(self, r=1):
        """Create a Circle with the given radius"""
        self.radius = r
        self.__class__.all_circles.append(self)
    def area(self):
        """determine the area of the Circle"""
        return self.__class__.pi * self.radius * self.radius
    def circumference(self):
        """determine the circumference of the Circle"""
        return self.__class__.pi * self.radius * 2

    @classmethod 
    def total_area(cls): 
        total = 0
        for c in cls.all_circles: 
            total = total + c.area()
        return total

    @classmethod 
    def total_circumference(cls): 
        total = 0
        for c in cls.all_circles: 
            total = total + c.circumference()
        return total

c1 = Circle(1)
c2 = Circle(2)
print(Circle.total_area())
print(Circle.total_circumference())
c2.radius=3
print(Circle.total_area())
print(Circle.total_circumference())

