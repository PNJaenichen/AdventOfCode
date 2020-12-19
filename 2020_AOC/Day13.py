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
print(f"You'll be waiting for Bus #{lowest[0]} for {lowest[1]} minutes ({lowest[0] * lowest[1]}).")

# Take the bus ideas and gather those needed along with their difference from 0-time
input_data = buses
bus_ids = []
for i, id in enumerate(input_data):
    if id != 'x':
        bus_ids.append((id, (id-i) % id))

# The initial timestamp can't be less than the first value
tmp = bus_ids[0][0]
timestamp, i = tmp, 0

# Chinese Remainder Theorem ... which honestly is magic. There are symbols on the wiki
# that I have never seen
loop = True
while loop:
    id, remainder = bus_ids[i+1]
    if (timestamp) % id  == remainder:
    # if the remainder from the enumeration is the same as with the timestamp ...
    # and we are at the end of the list of buses ...
        if i == len(bus_ids) - 2:
            # We've found the timestamp, print it and break the loop
            print(f"Timestamp of the earliest bus with subsequent offset: {timestamp}")
            loop = False
        # If not, then we increase to the next bus ID
        tmp *= id
        i += 1
    # If the timestamp and i,id remainders don't match, increase the timestamp and 
    # try again
    timestamp += tmp