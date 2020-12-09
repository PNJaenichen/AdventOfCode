# Get the Input, 9a is the example and 9b is the puzzle
with open('Day9a.txt') as f:
    cipher = []
    for line in f.readlines():
        cipher.append(line.strip())

# Set a constant variable for the preamble, test is 5 and puzzle is 25
PREAMBLE = 5



print(cipher)