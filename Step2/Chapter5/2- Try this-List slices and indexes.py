# Using what you know about the len() function and list slices, how would you combine
# the two to get the second half of a list when you don’t know what size it is? Experiment
# in the Python shell to confirm that your solution works.

x=[1,2,3,4,5]
print(x[len(x)//2:])