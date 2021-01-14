from statistics import mode

def seat_tester(value, rul):
    for rule in rul.values():
        for sect in rule[0]:
            if sect[0] <= value <= sect[1]:
                return True
    return False

# puzzle = "class: 1-3 or 5-7/nrow: 6-11 or 33-44/nseat: 13-40 or 45-50/n/nyour ticket:/n7,1,14/n/nnearby tickets:/n7,3,47/n40,4,50/n55,2,20/n38,6,12"

rules = {}
near_tickets = []

YOU = False

# for i, line in enumerate(puzzle.split('/n')):
with open('Day16a.txt') as f:
    for i, line in enumerate(f.readlines()): 
        if 'or' in line:
            section = line.split(':')[0]
            seats_one = tuple(int(x) for x in line.split(': ')[1].split(' or ')[0].split('-'))
            seats_two = tuple(int(x) for x in line.split(': ')[1].split(' or ')[1].split('-'))
            rules[section] = [[seats_one, seats_two], []]
        elif 'your' in line:
            YOU = True
        elif YOU:
            your_ticket = line.strip()
            YOU = False
        elif 'nearby' in line or line == '\n':
            continue
        else:
            near_tickets.append(line.strip())

invalid = []

for ticket in near_tickets:
    numbers = [int(x) for x in ticket.split(',')]
    for number in numbers:
        if seat_tester(number,rules):
            continue
        else:
            invalid.append(number)

print(f'The sum of all the invalid elements is {sum(invalid)}.')

good_tickets = []

for ticket in near_tickets:
    numbers = [int(x) for x in ticket.split(',')]
    if all(seat_tester(number, rules) for number in numbers):
        good_tickets.append(ticket)

for ticket in good_tickets:
    numbers = [int(x) for x in ticket.split(',')]
    for i, number in enumerate(numbers):
        for rule, value in rules.items():
            for sect in value[0]:
                if sect[0] <= number <= sect[1]:
                    rules[rule][1].append(i)