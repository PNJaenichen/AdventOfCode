# Get inputs from file
with open('Day6a.txt') as f:
    answers = []
    for line in f.readlines():
        answers.append(line.strip())

# Create a variable with a list of the possible questions
questions = 'abcdefghijklmnopqrstuvwxyz'

# Put all the groups into their own strings
group_answers = []
group = ""
for person in answers:
    if person == "":
        group_answers.append(group)
        group = ""
    else:
        group = group + person
group_answers.append(group)

# Initiate a count variable at 0
count = 0

# Iterate through each group, and then interate through the questions to see if
# Someone in the group answered yes
for grp in group_answers:
    for char in questions:
        if char in grp:
            count += 1

# Print the answer to Part 1
print(f'The passengers answered yes to a total of {count} questions')

# Combine the group answers into their own lists, and store in another list
group_lists = []
group = []
for person in answers:
    if person == "":
        group_lists.append(group)
        group = []
    else:
        group.append(person)
group_lists.append(group)

# Reset count to 0

count = 0

# Iterate through each group
for group in group_lists:
    # If their is only one member of the group, add the length to count
    if len(group) == 1:
        count += len(group[0])
    # Iterate through the questions
    else:
        for char in questions:
            check = []
            # Iterate through each member, if all marked yes, add True
            for member in group:
                if char in member:
                    check.append(True)
                else:
                    check.append(False)
            # If all answered True, increase the count by 1
            if all(check):
                count += 1

# This is the answer to Part 2
print(f'All members in a group answered yes to {count} questions amongst all passengers')




