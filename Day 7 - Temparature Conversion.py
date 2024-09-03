"""
Day 7 - Temparature Conversion
1. Write a program to convert temperature from Celsius to Fahrenheit. 
2. Write a program to convert temperature from Fahrenheit to Celsius
"""

def CelsiusToFahrenheit (celcius):
    fahrenheit = (celcius * 9/5) + 32
    return f"{fahrenheit:.2f}"

def FahrenheitToCelsius (farenheit):
    celcius = (farenheit - 32) * 5/9
    return f"{celcius:.2f}"


unit = ""

while  not unit == "C" and not unit == "F":
    print (f"UNIT: {unit}")
    unit = (input(f"Convert to C of F?: "))

temperature = float(input(f"Enter temperature to convert to {unit}: "))

if unit == "F":
    print (CelsiusToFahrenheit (temperature))
else:
    print (FahrenheitToCelsius (temperature))