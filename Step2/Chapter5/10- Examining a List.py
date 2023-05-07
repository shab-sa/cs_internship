# In this lab, the task is to read a set of temperature data (the monthly high temperatures
# at Heathrow Airport for 1948 through 2016) from a file and then find some basic
# information: the highest and lowest temperatures, the mean (average) temperature,
# and the median temperature (the temperature in the middle if all the temperatures are
# sorted).
# The temperature data is in the file lab_05.txt in the source code directory for this
# chapter. Because I haven’t yet discussed reading files, here’s the code to read the files
# into a list:
# temperatures = []
# with open('lab_05.txt') as infile:
# for row in infile:
# temperatures.append(int(row.strip())
# You should find the highest and lowest temperature, the average, and the median.
# You’ll probably want to use the min(), max(), sum(), len(), and sort()
# functions/methods.

temperatures = []
with open('lab_05.txt') as infile:
    for row in infile:
        temperatures.append(float(row.strip()))

print('The highest temperature is: ',max(temperatures))
print('The lowest temperature is: ',min(temperatures))
print('The average temperature is: ',sum(temperatures)/len(temperatures))
print('The median temperature is: ',sorted(temperatures)[len(temperatures)//2])
print(len(set(temperatures)))