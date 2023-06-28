# How would you use the os module’s functions to take a path to a file called test.log
# and create a new file path in the same directory for a file called test.log.old? How
# would you do the same thing using the pathlib module?

import os.path
old_path = os.path.abspath('test.log')
print(old_path)
new_path = f'{old_path}.old'
print(new_path)

import pathlib
path = pathlib.Path('test.log').resolve()
print(path)
new_path = f'{path}.old'
print(new_path)

# What path would you get if you created a pathlib Path object from os .pardir? Try it
# and find out.
# returns the parent of the current workin directory
print(pathlib.Path(os.pardir).resolve())