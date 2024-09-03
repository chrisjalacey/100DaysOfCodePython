"""Day 21 - Reverse List
Write a function to reverse a list."""

forwardList = [1,2,3,4,5]
backwardList = []
for i in range(1,len(forwardList)+1):
    print(forwardList[-i])
    backwardList.append(forwardList[-i])

print (backwardList)