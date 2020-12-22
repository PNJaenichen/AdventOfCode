from itertools import product

# This function will return the result of applying the bitmask to the supplied number
# The number needs to be the same length as the mask. This function follows the rules
# of Part 1
def bitmask(mask, number):
    mask = [char for char in mask]
    number = [char for char in number]
    for i in range(0,len(mask)):
        if mask[i] == 'X':
            continue
        else:
            if mask[i] == number[i]:
                continue
            else:
                number[i] = mask[i]
    return ''.join(number)

# This function will return the result of applying the bitmask to the supplied number
# and will return all the possible permutations of replacing X with both 1 and 0. This
# follows the rules for Part 2
def bitmask_two(mask, number):
    mask = [char for char in mask]
    number = [char for char in number]
    count = 0
    for i in range(0, len(mask)):
        if mask[i] == 'X':
            count += 1
            number[i] = mask[i]
        elif mask[i] == '1':
            number[i] = '1'
        else:
            continue
    perms = list(product([0, 1], repeat = count))
    for perm in perms:
        yield int(''.join(number).replace('X', '{}').format(*perm), 2)
    

# This is the Part 1 example
ex_inst = ['mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X','mem[8] = 11','mem[7] = 101','mem[8] = 0']

# This is the Part 2 example
ex_inst_two = ['mask = 000000000000000000000000000000X1001X','mem[42] = 100','mask = 00000000000000000000000000000000X0XX','mem[26] = 1']

# This opens the puzzle input and reads it into a single list
with open('Day14a.txt') as f:
    inst = []
    for line in f.readlines():
        inst.append(line.strip())

# Initiate a blank dictionary to store all the memory that is not set to 0
memory = {}

# Iterate through each element of the instructions
for item in inst:
    # If it's a mask, store it
    if 'mask' in item:
        mask = item[7:]
    # If it's not, get the memory location and the value, feed it to bitmask()
    else:
        mem, value = int(item.split('] = ')[0][4:]), int(item.split(' = ')[1])
        memory[mem] = int(bitmask(mask, bin(value).replace('0b','').zfill(36)), 2)

# Initiate the total variable
total = 0

# Iterate through each value in the dictionary and sum them
for value in memory.values():
    total += value

# This is the answer to Part 1
print(f'The total of memory from using Part 1 rules is {total}.')

# Reset the memory bank
memory = {}

# Iterate through each element of the instructions
for item in inst:
    # If it's a mask, store it
    if 'mask' in item:
        mask = item[7:]
    # If it's not, get the new memory location by feeding it to bitmask_two() and
    # then supply the value
    else:
        mem, value = int(item.split('] = ')[0][4:]), int(item.split(' = ')[1])
        for item in bitmask_two(mask,bin(mem).replace('0b','').zfill(36)):
            memory[item] = value

# Reset the total variable
total = 0

# Iterate through the values and get the total
for value in memory.values():
    total += value

# This is the answer to Part 2
print(f'The total of memory from using Part 2 rules is {total}.')