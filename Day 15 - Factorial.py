"""
Day 15 - Factorial
Write a function to calculate the factorial of a number.
"""

n = int(input("Enter integer: "))
factorial = 1
for i in range(2,n+1):
    factorial = factorial * i

print (f"The factorial of {n} is {factorial}")