codes = ['1-3 a: abcde','1-3 b: cdefg','2-9 c: ccccccccc']

with open('Day2a.txt') as codelist:
    codes = []
    for i in codelist.readlines():
        codes.append(i.strip())

sled_count = 0
toboggan = 0

for code in codes:
    password = code.split(':')
    required = password.pop(0).split(' ')
    numbers = required.pop(0).split('-')
    combined = [int(numbers[0]), int(numbers[1]), required[0], password[0].strip()]
    letter_count = 0
    for letter in combined[3]:
        if letter == combined[2]:
            letter_count += 1
    if letter_count in range(combined[0],combined[1]+1):
        sled_count += 1
    first = combined[3][combined[0]-1]
    second = combined[3][combined[1]-1]
    if combined[2] in [first, second] and first != second:
        print(combined[3], combined[2], first, second, True)
        toboggan += 1
    else:
        print(combined[3], combined[2], first, second, False)


print(f'There are {sled_count} per the sled rules, and {toboggan} per the Toboggan rules')

