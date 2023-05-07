# Which of the following will not be converted to numbers, and why?

#print(int('a1')) Error a1 is not a valid number
#print(int('12G', 16)) Error there is no G in base 16 numbers
print(float("12345678901234567890"))
#print(int("12*2")) Error Invalid literal for int( with base 10)