list= [[1, 2, 3], [2,1, 3], [4, 0, 1]]
def second_element(l):
    return l[1]
list.sort(key=second_element)
print(list)