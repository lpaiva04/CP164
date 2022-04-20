"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Lucas Paiva-Bernard
ID:      210985040
Email:   paiv5040@mylaurier.ca
__updated__ = "2022-01-10"
-------------------------------------------------------
"""
# Imports
from functions import is_leap_year

# Code

year = int(input("Enter a year: "))

leap_year = is_leap_year(year)

if leap_year == True:
    print (f"{year} is a leap year")
else:
    print (f"{year} is not a leap year")