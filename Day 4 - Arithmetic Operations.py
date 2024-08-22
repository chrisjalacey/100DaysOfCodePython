"""
Day 4 - Arithmetic Operations
1. Write a program that declares two integer variables and perform basic arithmetic operations 
    (addition, subtraction, multiplication, division) on them. Print the results to the console.
2. Write a program that calculates the area of a rectangle. 
    Prompt the user to input the length(integer) and width(integer) of the rectangle, calculate the area (length * width), and print the result.
3. Modify the above program to read decimal numbers as the length and width, and output the area to two decimal points

Reading List:
1. Learn about formatting options such as precision, alignment, and decimal places to present output in a clear and concise manner
"""

def mathOperations ():
    firstNumber = 1
    secondNumber = 2
    print (firstNumber + secondNumber)
    print (firstNumber - secondNumber)
    print (firstNumber * secondNumber)
    print (firstNumber / secondNumber)

#mathOperations ()

def areaOfRectangle ():
    length = float(input("Enter Length: "))
    width = float(input("Enter Width: "))

    #length = 5.001
    #width = 10.00004

    area = length * width

    print (f"Area: {area:.2f}")

areaOfRectangle ()

