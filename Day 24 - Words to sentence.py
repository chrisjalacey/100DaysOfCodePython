"""
Day 24 - Words to sentence.
Write a function to convert a list of words into a sentence.
"""

wordList = ["a","list","of", "words"]

wordString = ""

for i in wordList:
    wordString += i + " "

print (wordString)