import copy

# Get the puzzle input, 10a for the example and 10b for the puzzle inputs
with open('Day10b.txt') as f:
    adapt = []
    for line in f.readlines():
        adapt.append(int(line.strip()))

# Make a copy of adapt to work with it
adapters = copy.deepcopy(adapt)

# Initiate a variable to track joltage, single jolts, and triple jolts
joltage = 0
one_jolt = 0
three_jolt = 1

# Get the max size of the adapter in your bag
max_adapt = max(adapters)

# While adapter has items in it
while adapters:
    choices = []
    # Look for adapters that are within 3 of the current joltage
    for adapter in adapters:
        if adapter <= joltage + 3:
            choices.append(adapter)
    # Get the difference of the lowest possible number and the current joltage
    diff = min(choices) - joltage
    # Update the 1- and 3-jolt differences as appropriate
    if diff == 1:
        one_jolt += 1
    elif diff == 3:
        three_jolt += 1
    # Update the joltage to equal the lowest of the choices
    joltage = min(choices)
    # Remove the new adapter from the list of adapters
    adapters.remove(min(choices))

# This is the solution to part 1
print(f'The product of 1-jolt and 3-jolt differences is {one_jolt * three_jolt}.')

# Create a new copy of the adapters, add 0 and the device (max + 3)
perms = copy.deepcopy(adapt)
perms.append(0)
perms.append(max(perms)+3)

# Sort the list of adapters
sort_perms = sorted(perms)

# Intiate a variable to multiple the possible permutations
perm = 1

# Initiate a variable to track the lines and a list to make checks
line = 0
checks = []

# While the line counter is below the length of sorted list
while line < len(sort_perms) - 1:
    # Check to see if the next number in the list is 1 to 2 away
    if sort_perms[line + 1] - sort_perms[line] < 3:
        # If it is add it to checks list and increment the line
        checks.append(sort_perms[line])
        line += 1
    else:
        # Add the current line to the list, it's within 2 of the previous
        checks.append(sort_perms[line])
        # Check the length of check to get the possible permutations
        if len(checks) == 5:
            # Multiply it by the current number of permutations
            perm *= ((2**3) - 1)
        elif len(checks) == 4 or len(checks) == 3:
            perm *= (2**(len(checks) - 2))
        # Empty checks to start the process again
        checks = []
        # Increment the lines
        line += 1

# This is the solution for part 2
print(f'The total number of permutation is {perm}.')


    
