"""
Day 17 - Number of vowels in a string
Write a function to count the number of vowels in a string.
"""

input = "racecar"

vowels = ["a", "e", "i", "o", "u"]
counter = 0
for i in input:
    if i in vowels:
        counter+=1

print(f"Number of vowels in {input}: {counter}")