# Open the input file and read the information to a list of expenses
with open('Day1a.txt') as reports:
    expenses = []
    for i in reports.readlines():
        expenses.append(int(i.strip()))

# Function to find three numbers within a list that equal a certain value
def threeRes(ex, it):
    remain = 2020 - it
    j = 0
    while j < leng:
        if ex[j] == item:
            j += 1
        elif remain - ex[j] in ex:
            return item * expenses[j] * (remain - expenses[j])
        else:
            j += 1
    return ""

# Get the length of the expenses list
leng = len(expenses)

# Cycle through the list of expenses to find two that equal a certain value
for item in expenses:
    remain = 2020 - item
    # Once you find the remainder, search to see if that remainder is within the list and then break if it's found
    if remain in expenses:
        twoEntryResult = item * remain
        print(f"The two entry result is {twoEntryResult}")
        break
    else:
        continue

# Cycle through the list and run them through the three number function
for item in expenses:
    threeEntryResult = threeRes(expenses, item)
    if threeEntryResult:
        print(f"The three entry result is {threeEntryResult}")
        break
