# What code would you use to create a Rectangle class?

class Rectangle:
    def __init__(self):
        self.width = 2
        self.height = 4


rectangle = Rectangle()
a = (rectangle.width+rectangle.height)*2
print(f'Area of rectangle is {a}')
