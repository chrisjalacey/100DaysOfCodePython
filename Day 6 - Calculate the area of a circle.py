"""
Day 6 - Calculate the area of a circle.
Write a program that takes radius of the circle and outputs the area of the circle to 2 decimal digits
"""

pi = 3.14159
radius = float(input("Enter radius: "))
area = pi * (radius ** 2)
print(f"The area of the circle with radius {radius} is {area:.2f}")
