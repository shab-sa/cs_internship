from turtle import window_height


name = input("Name? ")
print(name)
age = int(input("Age? "))
# if the user provides a string the program will crashes with Value Error exception
print(age)
weight = float(input("Weight? "))
''' Here if we provide an integer number since implicit conversion from integer to float 
can be done by Pythin interpreter we will not get an error'''
print(weight)
