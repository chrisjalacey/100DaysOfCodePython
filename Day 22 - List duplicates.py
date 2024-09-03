"""Day 22 - List duplicates
Write a function to remove duplicates from a list."""

DuplicatesList = [1,2,4,3,4,5,5,4,4,4]
noDuplicatesList =[]

for i in DuplicatesList:
    if i not in noDuplicatesList:
        noDuplicatesList.append(i)

print(noDuplicatesList)