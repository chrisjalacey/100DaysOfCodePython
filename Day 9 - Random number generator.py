"""
Day 9 - Random number generator
1. Write a program that generates a random number. 
2. Write a program that generates random number between 2 integers

"""
import random

input1 = int(input("Enter integer 1: "))
input2 = int(input("Enter integer 2: "))

print (random.random())

print (random.randrange(input1,input2))
