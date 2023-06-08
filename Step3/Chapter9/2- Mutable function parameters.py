# What would be the result of changing a list or dictionary that was passed into a function
# as a parameter value? Which operations would be likely to create changes that would be
# visible outside the function? What steps might you take to minimize that risk?

# The changed list or dictionary would be visible outside the function except for reassigning
# or operations that creates a new list or dictionary

def f1(list):
    list.append(4)
    if len(list):
        list[0] = 123

def f2(dict):
    dict.setdefault(4,'4')
    

l = [1, 2, 3]
f1(l)
print(l)

d={1:'1',2:'2',3:'3'}
f2(d)
print(d)


