"""
Day 16 - Palindrome String
Write a function to check if a given string is a palindrome.
"""
palindrome = True
input = "racecara"
#print(input[-2])
for i in range(1,len(input)+1):
    if input[-i] != input[i-1]:
        print (f"{input} is not a palindrome")
        palindrome = False
        break


if palindrome is True:
    print (f"{input} is a palindrome")
