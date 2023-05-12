# What list comprehension would you use to process the list x so that all negative values
# are removed?

x = [1, 3, 5, 0, -1, 3, -2]
x_positive = [i for i in x if i > 0]
print(x_positive)

# Create a generator that returns only odd numbers from 1 to 100. (Hint: A number is
# odd if there is a remainder if divided by 2; use % 2 to get the remainder of division by
# 2.)

y = (i for i in range(100) if not i % 2)
for j in y:
    print(j, end=' ')
print('')

# Write the code to create a dictionary of the numbers and their cubes from 11 through 15.

z = {i: i**3 for i in range(11, 16)}
print(z)
