with open('test.txt', 'r') as file:
    contents = file.read()

items = contents.split()

frequency = {}

for item in items:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

for item, count in frequency.items():
    print(f'{item}: {count}')
