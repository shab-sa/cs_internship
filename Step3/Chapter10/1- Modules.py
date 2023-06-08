# Suppose that you have a module called new_math that contains a function called
# new_divide. What are the ways that you might import and then use that function?
# What are the pros and cons of each method?

# 1- from new_math import *
#    new_divide()
#    we can call the function without preceding it with the name of the module,
#    there may be conflicts with other functions with this name from other modules

# 2- import new_math
#    new_math.new_divide()
#    for accessing the function we need to write the name of the module before the name
#    of the function

# 3- from new_math import new_divide
#    new_divide()
#    only this function is accessible not other functions and variables

# Suppose that the new_math module contains a function call _helper_math(). How
# will the underscore character affect the way that _helper_math() is imported?

# this function can not be access if we use "from new_math import *", and somehow
# it is private to the module
