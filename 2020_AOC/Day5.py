# Open the input and create a list of all the boarding passes
with open('Day5a.txt') as f:
    boarding_passes = []
    for line in f.readlines():
        boarding_passes.append(line.strip())

# Initiatie a variable to track the highest seat ID
high_id = 0

# Create an array of empty seats 
empty_seats = []
for i in range(0,1022):
    empty_seats.append(i)

# Iterate through each boarding pass
for board in boarding_passes:
    # Setting the starting conditions to find the seat location
    rows = [0,128]
    cols = [0,8]
    # Iterate through each character of the boarding pass
    for i in range(0,10):
        # If 'F' then take half of the rows and subtract from the back
        if board[i] == "F":
            rows[1] = int(rows[1] - ((rows[1] - rows[0]) / 2))
        # If 'B' then take half of the rows and add to the front
        elif board[i] == "B":
            rows[0] = int(rows[0] + ((rows[1] - rows[0]) / 2))
        # If 'L' then take half of the columns and subtract from the right
        elif board[i] == "L":
            cols[1] = int(cols[1] - ((cols[1] - cols[0]) / 2))
        # Anything else is 'R' so take half of the columns add to the left
        else:
            cols[0] = int(cols[0] + ((cols[1] - cols[0]) / 2))
        # If it's digit 7 or 9, record the left value from the row/col
        if i == 6:
            row = rows[0]
        elif i == 9:
            col = cols[0]
    # Get the seat_id
    seat_id = (row * 8) + col
    # If the seat_id is in the empty_seats array, remove it because it's no
    # longer empty
    if seat_id in empty_seats:
        empty_seats.remove(seat_id)
    # If it's higher than the current high_id, then replace the high_id
    if seat_id > high_id:
        high_id = seat_id

# This is the answer to part 1
print(f'The highest seat ID is {high_id}')

# Iterate through each seat, if the empty lists has one higher or one lower
# it is not our seat and ignore it
for seat in empty_seats:
    if (seat - 1) in empty_seats or (seat + 1) in empty_seats:
        continue
    # The seat has does not have it's neighbor in the array is our seat
    else:
        my_seat = seat

# This is the answer to part 2
print(f'My seat ID is {my_seat}')
