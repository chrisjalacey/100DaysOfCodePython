"""
Day 29 - Words frequency
Create a dictionary of words and their frequencies.
"""

wordsDict = {}
sentence ="how many times are each word repeated in this sentence many or few"

for i in sentence.split():
    if i in wordsDict:
        wordsDict[i]+=1
    else:
        wordsDict[i]=1

print (wordsDict)

