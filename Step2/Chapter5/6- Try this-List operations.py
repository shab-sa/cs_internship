# If you have a list x, write the code to safely remove an item if—and only if—that value is in the list.

x = [0, 1, 1, 1, 2, 3, 4, 4, 5, 6, 3, 6, 7, 4, 3]
y = int(input("Insert a number: "))
if y in x:
    x.remove(y)
print(x)

# Modify that code to remove the element only if the item occurs in the list more than once.

x = [0, 1, 1, 1, 2, 3, 4, 4, 5, 6, 3, 6, 7, 4, 3]
y = int(input("Insert a number: "))
if x.count(y) > 1:  # y in x
    x.remove(y)
print(x)
