# Modify the Rectangle class’s code to make the dimension variables private. What
# restriction will this modification impose on using the class?
# this variable is not accessible outside the class or through class instance


class Rectangle:
    def __init__(self):
        self.__width = 4
        self.__height = 5

    def area(self):
        return (self.__width+self.__height)*2


rectangle = Rectangle()
print(f'Area of rectangle is {rectangle.area()}')
