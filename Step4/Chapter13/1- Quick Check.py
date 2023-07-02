# What is the significance of adding a "b" to the file open mode string, as in
# open("file", "wb")?

# It opens the file in binary format and Python makes no changeasto data as it
# is written to the file. It must be used when writing non-text files like images

# Suppose that you want to open a file named myfile.txt and write additional data on
# the end of it. What command would you use to open myfile.txt? What command
# would you use to reopen the file to read from the beginning?

with open('myfile.txt','a') as myfile:
    myfile.write('test123')

with open('myfile.txt','r', encoding='utf-8') as myfile:
    print(myfile.readline())
