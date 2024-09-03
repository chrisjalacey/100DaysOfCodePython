"""
Day 36 - Handle Exceptions I
Handle exceptions for division by zero.
"""
try:
    input1 = 1
    input2 = 0

    print (input1 / input2)

except ZeroDivisionError:
    print("you cannot divide by zero!")