temperatures = []
with open('lab_05.txt') as infile:
    for row in infile:
        temperatures.append(float(row.strip()))

print('The highest temperature is: ',max(temperatures))
print('The lowest temperature is: ',min(temperatures))
print('The average temperature is: ',sum(temperatures)/len(temperatures))
print('The median temperature is: ',sorted(temperatures)[len(temperatures)//2])
print(len(set(temperatures)))