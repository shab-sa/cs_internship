# Rewrite the code for a Rectangle class to inherit from Shape. Because squares and
# rectangles are related, would it make sense to inherit one from the other? If so, which
# would be the base class, and which would inherit?

# Yes it makes sense, the Rectangle is the super class and the Square which is kind of a
# special rectangle is the sub class.

# How would you write the code to add an area() method for the Square class? Should
# the area method be moved into the base Shape class and inherited by circle, square,
# and rectangle? If so, what issues would result?

# If the area method is moved into the base class, then it should be abstract and it should
# be implemented in each sub class.


class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, delta_x, delta_y):
        self.x = self.x + delta_x
        self.y = self.y + delta_y


class Circle(Shape):
    """Circle class"""
    all_circles = []
    pi = 3.14159

    def __init__(self, r=1, x=0, y=0):
        """Create a Circle with the given radius"""
        super().__init__(x, y)
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


class Square(Shape):
    def __init__(self, side=1, x=0, y=0):
        super().__init__(x, y)
        self.side = side

    def area(self):
        return self.side * 4


c = Circle(1)
c.move(3, 4)
print(c.x, c.y)
s = Square(5)
print(s.area())
