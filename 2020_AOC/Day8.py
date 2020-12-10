import copy

def boot_run(code):
    # Initiate a varible to track line in instructions
    line = 0   
    # Initiate varible to track accumulatr value
    acc = 0
    # Iterate through the lines
    while line < len(code):
    # Check to make sure the line has not been run before, if it has break
    # if it hasn't then increase the count by 1
        if code[line][0] != 0:
            break
        else:
            code[line][0] += 1
        if 'acc' in code[line][1]:
            acc += int(code[line][1][4:])
            line += 1
        elif 'jmp' in code[line][1]:
            if int(code[line][1][4:]) == 0:
                line += 1
            else:
                line += int(code[line][1][4:])
        else:
            line += 1
    return acc, line

# Get the input, 8a is the example input and 8b is the puzzle input
# with open('Day8a.txt') as f:
with open('Day8b.txt') as f:
    instruct = []
    for i in f.readlines():
        instruct.append(i.strip())

# Build a list of lists to track the number of times a line is executed
instructions = []
for row in instruct:
    instructions.append([0,row])

# This is the solution for Part 1
# print(f'The accumulator reaches {boot_run(instructions)[0]} before the infinite loop begins.')

# get a list of all the lines with 'jmp' and 'nop'
nop = []
jmp = []
for i in range(0,len(instructions)):
    if 'nop' in instructions[i][1]:
        nop.append(i)
    elif 'jmp' in instructions[i][1]:
        jmp.append(i)

# Iterate through each line and take turns replacing a 'nop' with 'jmp'
for entry in nop:
    test = copy.deepcopy(instructions)
    test[entry][1] = test[entry][1].replace('nop', 'jmp')
    result = boot_run(test)
    # If the boot_run function gets to the last line, print acc
    if result[1] == len(test):
        finished = [entry,result[0]]

# Same as above but replacing 'jmp' with 'nop'
for entry in jmp:
    test = copy.deepcopy(instructions)
    test[entry][1] = test[entry][1].replace('jmp', 'nop')
    result = boot_run(test)
    if result[1] == len(test):
        finished = [entry,result[0]]

# This is the solution for Part 2, comment out line 41 first
print(f'The accumulator reaches {finished[1]} when line {finished[0]} is changed.')