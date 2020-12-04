# Open the input file and save the ASCII maps for the hillside
with open('Day3a.txt') as snow:
    snowlines = []
    for i in snow.readlines():
        snowlines.append(i.strip())

# Function to move down the hill in a perscribed pattern, starting from the top left and working down the hill
def route_check(x_move, y_move, hill):
    trees = 0
    start_x = 0
    start_y = 0
    patt_length = len(hill[0])
    hill_height = len(hill)
    # Run this next bit until we make it to the bottom of the hill
    while start_y < hill_height:
        # Because the pattern repeats but the string does not, this wraps it around
        if start_x > patt_length - 1:
            start_x = start_x - patt_length
        # Get the character at the current location
        check = snowlines[start_y][start_x]
        if check == '#':
            trees += 1
        # Move down the hill and run it again
        start_x += x_move
        start_y += y_move
    return trees

# Create a list of the required routes, I made them tuples so as to not accidently change them
routes = [(1,1),(3,1),(5,1),(7,1),(1,2)]

# Total Trees are to be multiplied, so we initiate the variable at 1
total_trees = 1

# Run through the routes and get their results and mutliply them together
for route in routes:
    total_trees *= route_check(route[0],route[1],snowlines)

# This is the result for Part 1
print(f'There are {route_check(3,1,snowlines)} on the route.')

# This is the result for Part 2
print(f'There are {total_trees} on all the routes')

