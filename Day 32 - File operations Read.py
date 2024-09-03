"""
Day 32 - File operations: Read
Read and display the contents of a text file.
"""

file = "inputtext.txt"
with  open(file, "r") as f:
    text = f.readlines()
    for line in text:
        print (line)