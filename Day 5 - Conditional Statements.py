"""
Day 5 - Conditional Statements
1. Write a program that reads an integer as user input and prints whether the number is Odd or Even to the console
2. Write a program that takes three numbers as input and prints the largest among them
3. Write a program that checks if a given input year is a leap year or not
4. Write a program that reads the percentage and then prints their corresponding letter grade (A, B, C, D, or F)
"""

def oddOrEven ():
    inputInt = int(input("Enter an integer: "))
    if inputInt % 2 > 0:
        print ("Number is odd")
    else:
        print ("Number is even")

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

    
