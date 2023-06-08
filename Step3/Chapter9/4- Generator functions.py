# What would you need to modify in the previous code for the function four()to make it
# work for any number? What would you need to add to allow the starting point to also be
# set?

#def four():
    #x = 0
    #while x < 4:
        #print("in generator, x =", x)
        #yield x
        #x += 1

def four(y):
    x = y
    while True:  # x < 4:
        print("in generator, x =", x)
        yield x
        x += 1

# for i in four():
#    print(i)


5 in four(4)
