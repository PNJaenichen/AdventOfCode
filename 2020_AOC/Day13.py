# Create example inputs for time stamp and buses
ex_timestamp = 939
ex_buses = [7, 13, 'x', 'x', 59, 'x', 31, 19]

# Create Puzzle inputs for time stamp and buses
timestamp = 1014511
buses = [17,'x','x','x','x','x','x',41,'x','x','x','x','x','x','x','x','x',643,
'x','x','x','x','x','x','x',23,'x','x','x','x',13,'x','x','x','x','x','x','x','x',
'x','x','x','x','x','x','x',29,'x',433,'x','x','x','x','x',37,'x','x','x','x','x',
'x','x','x','x','x','x','x',19]

# Initiate variable to track lowest wait
lowest = None

# Iterate through all the buses
for x in buses:
    # If the bus equals x, skip to the next bus
    if x == 'x':
        continue
    else:
        # Find the closest bus departure AFTER the timestmap
        closest_stop = int((int(timestamp / x) + 1) * x)
        # Get the waittime between the depature and the timestamp
        wait = closest_stop - timestamp
        # If lowest is empty, fill it. If not, check to see if the new wait is lower
        if lowest == None:
            lowest = [x, wait]
        elif lowest[1] > wait:
            lowest = [x, wait]
        else:
            continue

# Print the bus ID by it's wait time for Part 1 Solution
print(lowest[0] * lowest[1])