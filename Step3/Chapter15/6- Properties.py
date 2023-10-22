# Update the dimensions of the Rectangle class to be properties with getters and
# setters that don’t allow negative sizes.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, width):
        if width < 0:
            raise ValueError("Width can not be negative")
        self.__width = width

    @height.setter
    def height(self, height):
        if height < 0:
            raise ValueError("Height can not be negative")
        self.__height = height

    def area(self):
        return (self.width+self.height)*2


rectangle = Rectangle(-3, 5)
rectangle.height = 5
print(f'Area of rectangle is {rectangle.area()}')
print(rectangle.height)





