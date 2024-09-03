"""
Day 14 - Leap Year
Write a program that checks if a given input year is a leap year or not
"""

from calendar import isleap
year = int(input("Enter year to check whether it is a leap year: "))
print (isleap(year))