# Get the Input, 9a is the example and 9b is the puzzle
with open('Day9b.txt') as f:
    cipher = []
    for line in f.readlines():
        cipher.append(int(line.strip()))

# Set a constant variable for the preamble, test is 5 and puzzle is 25
PREAMBLE = 25

# Iterate through each of the elements in list
for i in range(PREAMBLE,len(cipher)):
    # Create a list of values prior to the entry
    prior_v = cipher[i-PREAMBLE:i]
    check = []
    # Iterate through each of the prior values and check if the absolute value
    # can be found in the list
    for value in prior_v:
        if abs(cipher[i]-value) in prior_v:
            check.append(True)
        else: 
            continue
    # Check to see if any of the combinations could be added to get the entry
    if any(check):
        continue
    # If they can't, store the current entry as the invalid number and break
    # to get the first invalid number
    else:
        invalid_num = cipher[i]
        break

# This is the solution to Part 1
print(f'The first invalid number is {invalid_num}.')

# Iterate through all the numbers in the cipher            
for i in range(0,len(cipher)):
    total = 0
    inc = 0
    # Iterate through successive numbers and total them
    while total < invalid_num:
        total += cipher[i + inc]
        inc += 1
    # Once the total is at or above the invalid number, if it's equal than
    # provide the sum of the min and max of that number set
    if total == invalid_num:
        numbers = cipher[i:i+inc]
        if len(numbers) > 1:
            min_plus_max = min(numbers) + max(numbers)

# This is the solution to Part 2
print(f'The min + max for the consecutive numbers is {min_plus_max}.')



