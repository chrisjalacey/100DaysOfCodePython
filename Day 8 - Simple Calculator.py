"""
Day 8 - Simple Calculator
Create a simple calculator program that can add, subtract, multiply, and divide two integers
"""

input1 = int(input("Enter integer 1: "))
input2 = int(input("Enter integer 2: "))

operation = (input("Enter operation (+, -, * or /4): "))

print (eval (f"{input1} {operation} {input2}"))