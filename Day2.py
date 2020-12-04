# Open the input file and pull out the codes and their requirements
with open('Day2a.txt') as codelist:
    codes = []
    for i in codelist.readlines():
        codes.append(i.strip())

# Initiate the sled_count (for part 1) and tobaggan (for part 2) variables
sled_count = 0
toboggan = 0

# Work through each code in the list
for code in codes:
    # Split all the necessary parts and combine them into a more workable list
    password = code.split(':')
    required = password.pop(0).split(' ')
    numbers = required.pop(0).split('-')
    combined = [int(numbers[0]), int(numbers[1]), required[0], password[0].strip()]
    # Find the letter count for the required letter, regex might have been easier to use here
    letter_count = 0
    for letter in combined[3]:
        if letter == combined[2]:
            letter_count += 1
    # If the letter count is in the required range, count it is a good password
    if letter_count in range(combined[0],combined[1]+1):
        sled_count += 1
    # Pull the characters in the first and second position per the code requirement
    first = combined[3][combined[0]-1]
    second = combined[3][combined[1]-1]
    # Check to make sure that the required characters is one of the required two positions and not in both
    if combined[2] in [first, second] and first != second:
        toboggan += 1

# Print the results, sled_count is for part 1 and toboggan is for part 2
print(f'There are {sled_count} per the sled rules, and {toboggan} per the Toboggan rules')

