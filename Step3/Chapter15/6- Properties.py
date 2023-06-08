# Update the dimensions of the Rectangle class to be properties with getters and
# setters that don’t allow negative sizes.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.dimension = 2

    @property
    def dimension(self):
        return self.__dimension

    @dimension.setter
    def dimension(self, d):
        if d < 0:
            raise valueerror("Dimension can not be negative")
        self.__dimension = d

    def area(self):
        return (self.width+self.height)*2


rectangle = Rectangle(3, 5)
rectangle.dimension = 5
print(f'Area of rectangle is {rectangle.area()}')
print(rectangle.dimension)
