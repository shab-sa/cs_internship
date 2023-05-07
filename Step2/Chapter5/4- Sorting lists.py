# Suppose that you have a list in which each element is in turn a list: [[1, 2, 3], [2, 1, 3], [4, 0, 1]]. 
# If you wanted to sort this list by the second element in each list
# so that the result would be [[4, 0, 1], [2, 1, 3], [1, 2, 3]], what function
# would you write to pass as the key value to the sort() method?

list= [[1, 2, 3], [2,1, 3], [4, 0, 1]]
def second_element(l):
    return l[1]
list.sort(key=second_element)
print(list)