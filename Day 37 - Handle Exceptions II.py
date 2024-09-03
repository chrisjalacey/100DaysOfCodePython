"""
Day 37 - Handle Exceptions II
Handle exceptions for file not found.
"""

try:
    file = "inputte.txt"
    with  open(file, "r") as f:
        text = f.readlines()
        for line in text:
            print (line)

except FileNotFoundError:
    print("File not found")