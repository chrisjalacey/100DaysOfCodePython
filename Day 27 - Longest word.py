"""
Day 27 - Longest word
Find the longest word in a sentence.
"""

sentence = "what is the longest word in this sentence"
longestWord = ""
for i in sentence.split():
    if len(i) > len(longestWord):
        longestWord = i

print(longestWord)