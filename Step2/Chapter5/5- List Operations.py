# What would be the result of len([[1,2]] * 3)?

print(len([[1,2]] * 3)) #3

# What are two differences between using the in operator and a list’s index() method?

# Differences between in and index
# 1- index tells where in a list a value can be found 
# 2- in tells whether the value is in the list

# Which of the following will raise an exception?: min(["a", "b", "c"]); max([1, 2, "three"]); [1, 2, 3].count("one")

print(min(["a", "b", "c"]))
# print(max([1,2, "three"])) raise TypeError exception: '>' not supported between instances of 'str' and 'int'
print([1, 2, 3].count("one"))