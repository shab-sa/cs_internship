x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
import copy
y=copy.deepcopy(x)
y[0]=[0,0]
print(y)
print(x)