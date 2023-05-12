# Suppose that you have a list x = [1, 3, 5, 0, ­1, 3, ­2], and you need to
# remove all negative numbers from that list. Write the code to do this.

x = [1, 3, 5, 0, -1, 3, -2]
for i, v in enumerate(x):
    if v < 0:
        del x[i]
# x-positive=[i for i in x if i>0]
print(x)

# How would you count the total number of negative numbers in a list y = [[1, ­1,
# 0], [2, 5, ­9], [­2, ­3, 0]]?

y = [[1, -1, 0], [2, 5, -9], [-2, -3, 0]]
n = 0
for a in y:
    for b in a:
        if b < 0:
            n += 1
print(n)


# What code would you use to print very low if the value of x is below ­-5, low if it’s
# from -­5 up to 0, neutral if it’s equal to 0, high if it’s greater than 0 up to 5, and very
# high if it’s greater than 5?

x = 4

match x:
    case x if x < -5:
        print('nery low')
    case x if x < 0:
        print('low')
    case x if x == 0:
        print('neutral')
    case x if x < 5:
        print('high')
    case _:
        print('very high')
