# What would be in the variable x after the following snippets of code have executed?


x = "%.2f" % 1.1111 #1.11
print(x)
x = "%(a).2f" % {'a':1.1111} #1.11
print(x)
x = "%(a).08f" % {'a':1.1111} #1.11110000
print(x)