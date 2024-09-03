"""
Day 34 - File operations: Append
Append data to an existing text file.
"""
text = "1"
file = "appendtext.txt"

with  open(file, "a") as f:
    f.write(text)