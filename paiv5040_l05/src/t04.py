"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Lucas Paiva-Bernard
ID:      210985040
Email:   paiv5040@mylaurier.ca
__updated__ = "2022-02-19"
-------------------------------------------------------
"""
# Imports
from functions import to_power

# Code
base = float(input("Enter a base number: "))
power = int(input("Enter the exponent: "))


ans = to_power(base, power)

print (ans)