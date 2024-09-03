"""
Day 35 - File operations
Calculate the average of numbers in a text file.
"""

file = "inputnumbers.txt"
total = 0
with  open(file, "r") as f:
    text = f.readlines()
    for line in text:
        for number in line.split():
            total+=int(number)

print(total)