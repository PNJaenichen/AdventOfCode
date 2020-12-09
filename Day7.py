# Function to check for parent bags
def key_check(key, rule):
    # If Shiny Gold is in the list OR iterate through the keys of the 
    # current bag and check for shiny gold
    return any('shiny gold' in list(rule[key].keys()) or 
        key_check(keys, rule) for keys in rule[key])

# Function to check for the number of bags in a specified bag
def count_bag(key, rule):
    # Iterates through each key, gets the bag and the number of bags
    # Then checks the number of bags IN that bag, multiplies it by the
    # number of bags and then adds the bags themselves
    return sum([n + n * count_bag(keys, rule) 
        for keys, n in rule[key].items()])

# Get input, 7a is the example input and 7b is the puzzle input
with open('Day7b.txt') as f:
    instructions = []
    for line in f.readlines():
        instructions.append(line.strip())

# Initiate a dictionary to hold all the rules
rules = {}

# Parse the instructions to create a dictionary of dictionaries
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

# Initiate a variable to count the number of parent bags holding a Shiny gold bag
gold_count = 0

# Count the number of bags that return True for parent bags
for key in rules:
    if key_check(key,rules):
        gold_count += 1

# Print the results for Part 1
print(f'There are {gold_count} bags that can hold a shiny gold bag.')

# Print the results for Part 2
print(f'The shiny gold bag holds {count_bag("shiny gold", rules)} bags.')