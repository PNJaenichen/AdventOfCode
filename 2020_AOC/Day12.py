# Import regex and copy
import re
import copy
import math

# Get the direction to move/turn and units/degrees
def dir_parse(line):
    return line[0], int(re.search(r"\d+", line).group())

# Turn the ship
def head_change(cur_head, turn_direct, turn_amnt):
    HEADINGS = {0: 'N', 90: 'E', 180: 'S', 270: 'W'}
    # If the ship turns left, subtract
    if turn_direct == 'L':
        cur_head -= turn_amnt
    # If the ship turns right, add
    else: 
        cur_head += turn_amnt
    # If the heading is not between 0 and 359 ...
    while 0 > cur_head or cur_head >= 360:
        # If below 0, add 360
        if cur_head < 0:
            cur_head += 360
        # If at or above 360, then subtract 360 (while loop incase it's 720)
        else:
            cur_head -= 360
    # Return the numerical heading and compass heading
    return [cur_head, HEADINGS[cur_head]]

# Move the ship or the waypoint
def pos_change(cur_pos, compass, unit):
    # Check the compass direction and then move the ship that many units
    # Then return the new position
    if compass == 'E':
        cur_pos[0] += unit
    elif compass == 'W':
        cur_pos[0] -= unit
    elif compass == 'N':
        cur_pos[1] += unit
    else:
        cur_pos[1] -= unit
    return cur_pos

# Rotate the waypoint around the ship
def rotate_waypoint(cur_way, cur_pos, direct, units):
    # I don't understand why this works, it does not match the rotation around a
    # point mathmaticans that I found
    shifts = int(units/90)
    for shift in range(shifts):
        curr_E_W = cur_way[0]
        curr_N_S = cur_way[1]
        if direct == 'L':
            cur_way[0] = curr_N_S - (curr_N_S * 2)
            cur_way[1] = curr_E_W
        elif direct == 'R':
            cur_way[0] = curr_N_S
            cur_way[1] = curr_E_W - (curr_E_W * 2)
    return cur_way

# Move the ship to the waypoint
def move_ship(cur_pos, cur_way, units):
    return [cur_pos[0] + (cur_way[0] * units), cur_pos[1] + (cur_way[1] * units)]

# calculate manhattan distance from origin, the sum of the absolute values of x & y
def manhattan(cur_pos):
    return abs(cur_pos[0]) + abs(cur_pos[1])

# Take in and parse the input
with open('Day12b.txt') as f:
    instruct = []
    for line in f.readlines():
        instruct.append(line.strip())

# Making a working copy of the input
instructions = copy.deepcopy(instruct)

# Ship's starting location is the origin and heading is E (or 90)
position = [0,0]
heading = [90, 'E']

# Command the ship ...
for line in instructions:
    # Get the command
    direct, units = dir_parse(line)
    # If it's to turn ... turn
    if direct in ['L','R']:
        heading = head_change(heading[0], direct, units)
    # If it's to go forward, get the current compass heading then move
    elif direct == 'F':
        position = pos_change(position, heading[1], units)
    # Move the compass heading
    else:
        position = pos_change(position, direct, units)

# Print the solution to Part 1
print(f'The Part 1 Manhattan distance is {manhattan(position)}')

# Reset the ships position, heading, and add waypoint location for Part 2
position = [0,0]
heading = [90,'E']
waypoint = [10,1]

# Command the ship again ... 
for line in instructions:
    # Get the command
    direct, units = dir_parse(line)
    # If it's to move the ship
    if direct == 'F':
        position = move_ship(position, waypoint, units)
    # If it's to rotate the waypoint
    elif direct in ['L','R']:
        waypoint = rotate_waypoint(waypoint, position, direct, units)
    # If it's to move the waypoint
    else:
        waypoint = pos_change(waypoint, direct, units)

# Print the solution to Part 2
print(f'The Part 2 Manhattan distance is {manhattan(position)}')

