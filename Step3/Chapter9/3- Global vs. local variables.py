# Assuming that x = 5, what will be the value of x after funct_1() below executes?
# After funct_2() executes?

x = 5

def funct_1():
    x = 3

funct_1()
print(x)  # 5

def funct_2():
    global x
    x = 2

funct_2()
print(x)  # 2
