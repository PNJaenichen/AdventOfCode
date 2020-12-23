# This takes the next number along with the dictionary
def next_number(num, track):
    # If the number is in the track, but it was just called return 0 for being
    # the first time
    if num in track and len(track[num]) == 1:
        return 0
    else:
        # Else, get the difference of the most two most recent turns
        # turns = sorted(track[num], reverse=True)
        # return turns[0] - turns[1]
        return track[num][-1] - track[num][-2]

# This is the example or puzzle inputs
# puzzle = [0,3,6]
puzzle = [18,11,9,0,5,1]

# Initiate the  track dictionary
turn_tracker = {}

# Initiate the count at 1 to track the turns
count = 1

# The first turns are the starting numbers, add them and increase the count
for item in puzzle:
# for item in example:
    turn_tracker[item] = [count]
    count += 1

# Start the new number as the last item in our starting input
newNum = puzzle[-1]

# While the count is less than the required number
while count < 30000001:
    # Get the next number
    newNum = next_number(newNum, turn_tracker)
    # If it's not in the tracker, add it with the turn as the start of its list
    if newNum not in turn_tracker:
        turn_tracker[newNum] = [count]
    # If it is add the turn to it's list of turns
    else:
        turn_tracker[newNum].append(count)
        while len(turn_tracker[newNum]) > 2:
            turn_tracker[newNum].pop(0)
    # Print the answer to Part 1 when we reach turn 2020
    if count == 2020:
        print(f'The number on the 2020th turn is {newNum}')
    # Increase the turn count by 1
    count += 1

# Print the answer to Part 2 when we reach turn 30,000,000
print(f'The number on the 30 milionth turn is {newNum}.')
