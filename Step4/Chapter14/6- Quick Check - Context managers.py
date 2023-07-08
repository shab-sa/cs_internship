# Assume that you’re using a context manager in a script that reads and/or writes several
# files. Which of the following approaches do you think would be best?
# Put the entire script in a block managed by a with statement.
# Use one with statement for all file reads and another for all file writes.
# Use a with statement each time you read a file or write a file (for each line, for
# example).
# Use a with statement for each file that you read or write.

# I think I am more comfortable with using one with and definig all file objects like:
# with open('file1.txt') as file1,open('file2.txt','w')as file2:
