# Suppose that you’re writing a program that works like a spreadsheet. How might you
# use a dictionary to store the contents of a sheet? Write some sample code to both store
# a value and retrieve a value in a particular cell. What might be some drawbacks to this
# approach?

spreadshit = {'name': ['sara', 'simin', 'susan'],
              'family': ['ahmadi', 'ashuri', 'ashtari'],
              'age': [21, 22, 23]}
spreadshit['name'].append('sina')
print(spreadshit['name'])
print(spreadshit['name'][-1])
