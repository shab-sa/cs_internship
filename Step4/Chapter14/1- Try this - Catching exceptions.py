# Write code that gets two numbers from the user and divides the first number by the
# second. Check for and catch the exception that occurs if the second number is zero
# (ZeroDivisionError).


a=int(input('Enter first number: '))
b=int(input('Enter second number: '))
try:
    print(f'The division of two numbers is equal to: {a//b}')
except ZeroDivisionError:
    print('Division by zero is not allowed.')