"""Day 13 - Largest of three numbers.
Write a program to find the largest of three numbers.
"""

def largestNumber ():
    inputList = list()
    inputList.append(int(input("Enter integer 1: ")))
    inputList.append(int(input("Enter integer 2: ")))
    inputList.append(int(input("Enter integer 3: ")))

    largest = inputList[0]
    for i in inputList:
        if i > largest:
            largest = i
    return largest
print (largestNumber ())

    
