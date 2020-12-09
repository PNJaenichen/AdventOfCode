def key_check(key, rule):
    for keys in rule[key]:
        if 'shiny gold' in list(rule[key].keys()):
            return True
        elif key_check(keys,rule):
            return True
        else:
            return key_check(keys,rule)

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

gold_count = []

for key in rules:
    if key_check(key, rules):
        gold_count.append(key)
        
<<<<<<< HEAD
print(gold_count, len(gold_count))
=======
print(gold_count, len(gold_count))
>>>>>>> c87746bacd41c32735663a2f1ea25c718bdd0687
