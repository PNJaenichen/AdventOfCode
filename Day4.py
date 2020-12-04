# Import the regex library
import re

# Import the information from the input file
with open('Day4a.txt') as f:
    info = []
    for line in f.readlines():
        info.append(line.strip())

# Set up the list and dictionary to build each of the individual dictionaries
passports = []
passport = {}

# Roll through each of the lines in the info list
for line in info:
    # If the line is empty, the passport information is complete, add it to passports and ready the passport for the next one
    if line == "":
        passports.append(passport)
        passport = {}
    # If it's not empty, split the lines into the parts and then split them again to get the Key:Value pairs
    else:
        line_break = line.split(" ")
        for piece in line_break:
            parts = piece.split(":")
            passport[parts[0]] = parts[1]
# After the last line, add the final passport to the list of passports
passports.append(passport)

# Initiative the valid_passes variable at 0 in order to start the count
valid_passes = 0

# This is for part 1
for passport in passports:
    # Get a list of the keys from the passport
    pass_keys = list(passport.keys())
    # If there are less than 7 keys, it's invalid
    if len(pass_keys) < 7:
        continue
    # If it has exactly 7 keys and cid is part of it, it's invalid
    elif len(pass_keys) == 7 and 'cid' in pass_keys:
        continue
    # Everything else is valid
    else:
        valid_passes += 1

# Print the results for Part 1
print(f'{valid_passes} passport(s) have the required information')

# Reset valid_passes to prepare for step 0
valid_passes = 0

# This one starts the same as Part 1, until we get to the passports with the correct keys
for passport in passports:
    pass_keys = list(passport.keys())
    if len(pass_keys) < 7:
        continue
    elif len(pass_keys) == 7 and 'cid' in pass_keys:
        continue
    else:
        # Roll through each of the elements and ensure that they meet the validity requirements
        # This could probably be improved with functions
        if int(passport['byr']) in range(1920,2003):
            if int(passport['iyr']) in range(2010,2021):
                if int(passport['eyr']) in range(2020,2031):
                    if re.fullmatch(r'[#][a-zA-Z0-9]{6}', passport['hcl']):
                        if passport['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth']:
                            if re.fullmatch(r'[0-9]{9}', passport['pid']):
                                if 'cm' in passport['hgt']:
                                    if int(passport['hgt'].replace('cm','')) in range(150,194): 
                                        valid_passes += 1
                                if 'in' in passport['hgt']:
                                    if int(passport['hgt'].replace('in','')) in range(59,77):
                                        valid_passes += 1

# Print the results for Part 2             
print(f'{valid_passes} passport(s) meet the validity requirements.')
