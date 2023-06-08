# How would you modify the code for the decorator function to remove unneeded
# messages and enclose the return value of the wrapped function in "<html>" and "
# </html>", so that myfunction ("hello") would return "<html>hello<html>"?


def decorate(func):
    # print("in decorate function, decorating", func.__name__)
    def wrapper_func(*args):
        # print("Executing", func.__name__)
        return func(("<html>{0}</html>".format(*args)))
    return wrapper_func


@decorate
def myfunction(parameter):
    print(parameter)


myfunction("hello")
