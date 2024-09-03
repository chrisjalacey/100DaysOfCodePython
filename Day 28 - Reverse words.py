"""
Day 28 - Reverse words
Reverse words in a sentence.
"""
sentence = "reverse this sentence code will"
backwardsSentence = ""

print (sentence)


for i in range(1,len(sentence.split())+1):
    backwardsSentence+=f"{sentence.split()[-i]} "

print (backwardsSentence)