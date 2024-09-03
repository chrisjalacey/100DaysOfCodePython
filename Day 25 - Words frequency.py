"""Day 25 - Words frequency
Write a function to count the frequency of words in a sentence."""

wordsDict = {}
sentence ="how many times are each word repeated in this sentence many or few"

for i in sentence.split():
    if i in wordsDict:
        wordsDict[i]+=1
    else:
        wordsDict[i]=1

print (wordsDict)

