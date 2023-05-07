# What would be a quick way to change all punctuation in a string to spaces?

import string
x = 'Hello, world!a'
table = x.maketrans(string.punctuation,' '*len(string.punctuation)) #('', '', string.punctuation)  # (',.!?', '    ')
print(x.translate(table))
