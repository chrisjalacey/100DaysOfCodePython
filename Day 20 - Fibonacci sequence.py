"""
Day 20 - Fibonacci sequence
Write a function to calculate the Fibonacci sequence up to a certain limit.
"""
lower = 1
upper = 2
while upper < 100:
    inter = upper
    upper = lower + upper
    lower = inter

    print (upper)