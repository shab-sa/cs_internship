# 1;  ok
# Decide which of the following expressions can be a dictionary key:

# 'bob'; ok
# ('tom', [1, 2, 3]); not ok
# ["filename"]; not ok
# "filename"; ok
# ("filename","extension") ok
x = {1: 1, 'bob': 2, "filename": 5, ("filename", "extension"): 6}
print(x)
