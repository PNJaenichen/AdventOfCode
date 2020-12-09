def key_check(key, rule):
    return any('shiny gold' in list(rule[key].keys()) or 
        key_check(keys, rule) for keys in rule[key])

def count_bag(key, rule):
    return sum([n + n * count_bag(keys, rule) 
        for keys, n in rule[key].items()])

# Get input
with open('Day7b.txt') as f:
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
            bag[parts[1][j][1]] = int(parts[1][j][0])
    rules[parts[0]] = bag

gold_count = []

for key in rules:
    if key_check(key,rules):
        gold_count.append(key)

print(f'There are {len(gold_count)} bags that can hold a shiny gold bag')

print(count_bag('shiny gold', rules))