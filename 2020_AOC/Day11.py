# import copy to make create copies of lists to work with
import copy

# This gets the immediately adjacent (diaganol and orthoganal) neighbors to a seat
def seat_check(rows, cols, lay):
    adj_seats = []
    rows_len = len(lay)
    cols_len = len(lay[rows])
    for row in range(rows-1, rows+2):
        # Iterate through the range above, as long as it's between 0 and the end 
        # of the list
        if 0 <= row < rows_len:
            for col in range(cols-1, cols+2):
                # Iterate through the range above as long as it's between 0 and
                # the end of the row
                if 0 <= col < cols_len:
                    cur_seat = lay[row][col]
                    # If the current seat doesn't equal the supplied seat and
                    # it is occupied, add it to the list
                    if (rows, cols) != (row, col) and cur_seat == "#" :
                        adj_seats.append(cur_seat)
    # Return the list containing any occupied seats
    return adj_seats

# This gets the first seat that is visible along each of the axis away from the
# supplied seat
def find_adj_seats(seating_placements, cur_seat_row, cur_seat_col):
    adj_seats = []
    row_len = len(seating_placements)
    col_len = len(seating_placements[cur_seat_row])
    adj_adjustments = [(row_adj, col_adj) for row_adj in [-1, 0, 1] for col_adj in [-1, 0, 1]]
    # Work through each of the possible adjustments
    for adjustment in adj_adjustments:
        row_adj, col_adj = adjustment
        # Make the adjustments to the row and col
        row, col = cur_seat_row + row_adj, cur_seat_col + col_adj
        # As long as the row and col are within the limits of the seating layout
        # then continue
        while 0 <= row < row_len and 0 <= col < col_len:
            # If row and col are at 0,0 (meaning supplied seat) then break and 
            # move on to the next so you stay out of an inifinte loop
            if row_adj == 0 and col_adj == 0:
                break
            cur_seat = seating_placements[row][col]
            # If the current seat isn't the floor ...
            if cur_seat != ".":
                # And it's occupied
                if cur_seat == "#":
                    # Add it to the list
                    adj_seats.append(cur_seat)
                break
            # continue along the path
            row += row_adj
            col += col_adj
    # Return the list of any occupied seats
    return adj_seats

# For Part 2, takes the current layout and applies the Part 2 rule changes
def take_seats(lay):
    # Create a blank layout
    current_layout = []
    # Iterate through each row
    for i in range(0,len(lay)):
        # Create a blank row
        new_row = []
        # Iterate through each column
        for j in range(0,len(lay[i])):
            # Get the current seat and it's surrounding neighbors
            cur_seat = lay[i][j]
            surround = find_adj_seats(lay, i, j)
            # If the seat is empty ...
            if cur_seat == 'L':
                # And there are no visible occupied seats, occupy the current seat
                if len(surround) == 0:
                    new_row.append('#')
                # Or leave it empty
                else:
                    new_row.append('L')
            # If the seat is occupied ...
            elif cur_seat == '#':
                # If there are 5 or more visible occupied seats, then get up
                if len(surround) >= 5:
                    new_row.append('L')
                # Or remained seated and occupied
                else:
                    new_row.append('#')
            # If it's the floor, just add it to the row
            else:
                new_row.append(cur_seat)
        # Add the new row to the new layout
        current_layout.append(new_row)
    # If the new layout doesn't match the provided layout then changes were made
    # Return the new layout and True
    if current_layout != lay:
        return current_layout, True
    # Or return what is now the final layout and false
    else:
        return current_layout, False

# Get the puzzle inputs, Day11a for the example and Day11b for the puzzle
with open('Day11b.txt') as f:
    seats = []
    for row in f.readlines():
        # Strip the newline, add in spaces and then split at the spaces 
        seats.append(row.strip().replace('', ' ').split())

# Create a working copy of the input
origin_layout = copy.deepcopy(seats)

# Create a blank current layout
current_layout = []

# Get the size of the layout
room_size = (len(origin_layout[0]), len(origin_layout))

# Initiate a change flag
no_change_flag = True

# Initiate a variable to count the iterations
count = 0

# While there are changes being made to the layout ...
while no_change_flag:
    # Iterate through each line of the layout
    for i in range(0,room_size[1]):
        # Create a new line
        new_row = []
        # Iterate through each seat/floor spot in the layout
        for j in range(0,room_size[0]):
            # Check it's immediate neighbors
            surround = seat_check(i,j,origin_layout)
            # If it's an empty seat ...
            if origin_layout[i][j] == 'L':
                # And there are no occupied seats ... 
                if '#' not in surround:
                    # Occupy it ...
                    new_row.append('#')
                else:
                    # Or leave it empty ... 
                    new_row.append('L')
            # If it's an occupied seat ...
            elif origin_layout[i][j] == '#':
                # And there are more then 4 occupied neighbors ...
                if surround.count('#') >= 4:
                    # Leave the seat
                    new_row.append('L')
                else:
                    # Or occupy it
                    new_row.append('#')
            # Add the floor to the row to maintain the grid, this is mostly
            # for troubleshooting
            else:
                new_row.append(origin_layout[i][j])
        # Add this new row to the current layout
        current_layout.append(new_row)
    # If the original and current layouts do not match, then changes were made
    if origin_layout != current_layout:
        # Copy the current to the origin and clear the current
        origin_layout = copy.deepcopy(current_layout)
        current_layout = []
    # They match, no changes were made, change flag to False to stop the loop
    else:
        no_change_flag = False
    # Increase the iterations by 1
    count += 1

# Initiate a variable to count occupied seats
occ_count = 0

# Iterate through each row and count the number of occupied seats
for row in origin_layout:
    occ_count += row.count('#')

# This is the solution to Part 1
print(f'With Part 1 Rules, there were {occ_count} occupied seats after {count} iterations.')

# Create a new working copy of the original input
origin_layout = copy.deepcopy(seats)

# Reset the count and occ_count variables to 0
count = 0
occ_count = 0

# Get the first layout from the take_seats function
layout, changes = take_seats(origin_layout)
# Continue to run take_seats until it flags false after no changes are made
while changes:
    layout, changes = take_seats(layout)
    # Get the count of iterations
    count += 1
# Iterate through each line and count of occupied seats
for row in layout:
    occ_count += row.count('#')

# This is the solution to Part 2
print(f'With Part 2 Rules, there were {occ_count} occupied seats after {count} iterations.')