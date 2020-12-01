with open('Day1a.txt') as reports:
    expenses = []
    for i in reports.readlines():
        expenses.append(int(i.strip()))

leng = len(expenses)
j = 0

for item in expenses:
    remain = 2020 - item
    if remain in expenses:
        twoEntryResult = item * remain
        print("The two entry result is " + twoEntryResult)
        break
    else:
        continue

for item in expenses:
    remain = 2020 - item
    j = 0
    while j < leng:
        if expenses[j] == item:
            j += 1
        elif remain - expenses[j] in expenses:
            threeEntryResult = item * expenses[j] * (remain - expenses[j]))
            print("The three entry result is " + threeEntryResult)
            break
        else:
            j += 1
