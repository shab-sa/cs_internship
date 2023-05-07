# How could you use split and join to change all the whitespace in string x to dashes,
#such as changing "this is a test" to "this­is­a­test"?

string="this is a test"
list=string.split(' ')
new_string='-'.join(list)
print(new_string)