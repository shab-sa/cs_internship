# Explain why the following operations aren’t legal for the tuple x = (1, 2, 3, 4):
# x.append(1)
# x[1] = "hello"
# del x[2]

# Tuple are of immutable types, this means once they are defined, they can't be changed anymore
# so expression like these:
# x = (1, 2, 3, 4):
# x.append(1)
# x[1] = "hello"
# del x[2]
# would result in error

# If you had a tuple x = (3, 1, 4, 2), how might you end up with x sorted?

x = (3, 1, 4, 2)
x=tuple(sorted(x))
print(x)