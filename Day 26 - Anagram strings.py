"""
Day 26 - Anagram strings
Write a function check if two strings are anagrams.
"""

string1 = "abc"
string2 = "cba"

print(sorted(string1))
print(sorted(string2))

if sorted(string1) == sorted(string2):
    print (f"{string1} and {string2} are anagrams")
else:
        print (f"{string1} and {string2} are not anagrams")