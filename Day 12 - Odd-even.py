"""Day 12 - Odd-even
Write a program to check if a number is even or odd.
"""

def oddOrEven ():
    inputInt = int(input("Enter an integer: "))
    if inputInt % 2 > 0:
        print ("Number is odd")
    else:
        print ("Number is even")

oddOrEven ()