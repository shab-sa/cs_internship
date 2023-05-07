# If the string x equals "(name, date),\n", which of the following would return a string containing "name, date"?

x= "(name, date),\n"
print(x.rstrip("),"))
print(x.strip("),\n"))
print(x.strip("\n)(,")) #prints the "name, date"
