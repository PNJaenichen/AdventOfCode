import re

with open('Day4a.txt') as f:
    info = []
    for line in f.readlines():
        info.append(line.strip())

passports = []
passport = {}

for line in info:
    if line == "":
        passports.append(passport)
        passport = {}
    else:
        line_break = line.split(" ")
        for piece in line_break:
            parts = piece.split(":")
            passport[parts[0]] = parts[1]
passports.append(passport)

valid_passes = 0

for passport in passports:
    pass_keys = list(passport.keys())
    if len(pass_keys) < 7:
        continue
    elif len(pass_keys) == 7 and 'cid' in pass_keys:
        continue
    else:
        valid_passes += 1

print(f'{valid_passes} passport(s) have the required information')

valid_passes = 0

for passport in passports:
    pass_keys = list(passport.keys())
    if len(pass_keys) < 7:
        continue
    elif len(pass_keys) == 7 and 'cid' in pass_keys:
        continue
    else:
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

print(f'{valid_passes} passport(s) meet the validity requirements.')
