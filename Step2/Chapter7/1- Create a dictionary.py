# Write the code to ask the user for three names and three ages. After the names and ages
# are entered, ask the user for one of the names, and print the correct age.

name_age_dic={}
names=input("Enter 3 names: ").split()
ages=input("Enter 3 ages: ").split()
for i,name in enumerate(names):
    name_age_dic[name]=ages[i]
name=input('Enter one of the names you entered before: ')
print(f'{name} is {name_age_dic[name]} years old:)')