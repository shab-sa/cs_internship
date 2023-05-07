# Tuple are of immutable types, this means once they are defined, they can't be changed anymore
# so expression like these:
# x = (1, 2, 3, 4):
# x.append(1)
# x[1] = "hello"
# del x[2]
# would result in error

x = (3, 1, 4, 2)
x=tuple(sorted(x))
print(x)