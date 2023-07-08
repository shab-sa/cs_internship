# Do Python exceptions force a program to halt?
# Suppose that you want accessing a dictionary x to always return None if a key doesn’t
# exist in the dictionary (that is, if a KeyError exception is raised). What code would you
# use?


# No they don't halt the program

x = {'a': 1, 'b': 2}
try:
    # v=x['a']
    v = x['c']
except KeyError as e:
    v = None

print(v)
