"""
Day 19 - Maximum in List
Write a function to find the maximum element in a list."""

def largestNumber ():
    inputList = [5, 1, 2, 3, 4]

    largest = inputList[0]
    for i in inputList:
        if i > largest:
            largest = i
    return largest
print (largestNumber ())

    
