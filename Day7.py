# Get input
with open('Day7a.txt') as f:
    instructions = []
    for line in f.readlines():
        instructions.append(line.strip())

rules = {}

for i in instructions:
    i = i.replace('.','')
    parts = i.split(' contain ')
    parts[0] = parts[0].replace(' bags','')
    if parts[1] != 'no other bags':
        parts[1] = parts[1].split(', ')
    bag = {}
    for j in range(0,len(parts[1])):
        if parts[1] != 'no other bags':
            if 'bags' in parts[1][j]:
                parts[1][j] = parts[1][j].replace(' bags', '')
            else:
                parts[1][j] = parts[1][j].replace(' bag', '')
            parts[1][j] = parts[1][j].split(' ', 1)
            bag[parts[1][j][1]] = parts[1][j][0]
    rules[parts[0]] = bag

for key in rules:
    print(key, rules[key])