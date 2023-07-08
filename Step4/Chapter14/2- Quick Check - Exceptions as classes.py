# If MyError inherits from Exception, what is the difference between except
# Exception as e and except MyError as e?

# If we use Exception, then we are using the base class and in the output there will be no
# sign that the actual error was raised due to MyError exception and it could be raised by
# other exceptions that ingerits from the Exception class.
