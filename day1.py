with open('Day1a.txt') as reports:
    expenses = []
    for i in reports.readlines():
        expenses.append(int(i.strip()))

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


leng = len(expenses)

for item in expenses:
    remain = 2020 - item
    if remain in expenses:
        twoEntryResult = item * remain
        print(f"The two entry result is {twoEntryResult}")
        break
    else:
        continue

for item in expenses:
    threeEntryResult = threeRes(expenses, item)
    if threeEntryResult:
        print(f"The three entry result is {threeEntryResult}")
        break
