x = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# Assume that you have a dictionary x = {'a':1, 'b':2, 'c':3, 'd':4} and a
# dictionary y = {'a':6, 'e':5, 'f':6}. What would be the contents of x after the
# following snippets of code have executed?:
# del x['d']
# z = x.setdefault('g', 7)
# x.update(y)

y = {'a': 6, 'e': 5, 'f': 6}
del x['d']  # remove 'd' entry from dictionary x = {'a':1, 'b':2, 'c':3}
z = x.setdefault('g', 7)  # add an entry with key 'g' and value 7
# update key a with value 6 and add e and f to x, x = {'a':6, 'b':2, 'c':3, 'g':7, 'e':5, 'f':6}
x.update(y)
print(x)
