# Modify the Rectangle class’s code to make the dimension variables private. What
# restriction will this modification impose on using the class?
# this variable is not accessible outside the class or through class instance

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__dimension = 2

    def area(self):
        return (self.width+self.height)*2


rectangle = Rectangle(3, 5)
print(f'Area of rectangle is {rectangle.area()}')
#print(rectangle.__dimension)
