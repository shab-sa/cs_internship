# How would you write a function that could take any number of unnamed arguments
# and print their values out in reverse order?

def print_reverse(*num):
    print(num[::-1])


print_reverse(1, 2, 3, 4, 5, 6)
# What do you need to do to create a procedure or void function—that is, a function with
# no return value?


def test():
    return None


print(test())
# What happens if you capture the return value of a function with a variable?
# we can use that returned value again because it is stored in a variable


def capture_value(num):
    return num*num


print(capture_value(4))
