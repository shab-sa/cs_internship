# How might you calculate the total size of all files ending with .txt that aren’t symlinks in
# a directory? If your first answer was using os.path, also try it with pathlib, and vice
# versa.

# import os
# total_size=0
# with os.scandir('.') as mydir:
#     for dir in mydir:
#         print(dir.name)
#         if not dir.is_symlink():
#             if os.path.splitext(dir)[1]=='.txt':
#                 total_size+= os.path.getsize(dir) #dir.stat().st_size 
#                 os.mkdir('backup')
#                 os.rename(dir,os.path.join('.','backup',os.path.basename(dir)))

# print(total_size)

import pathlib
ts=0
for dir in pathlib.Path('.').iterdir():
    if not dir.is_symlink():
        if dir.suffix=='.txt':
            ts+= pathlib.Path(dir).stat().st_size
            new_path=pathlib.Path('bakcup')
            new_path.mkdir()
            dir.rename(pathlib.Path( new_path,dir.name))

print(ts)

# Write some code that builds off your solution to move the same .txt files in the lab
# question to a new subdirectory called backup in the same directory.