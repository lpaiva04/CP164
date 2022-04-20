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
from functions import is_palindrome

# Code

s = str(input("Enter a string: "))

palindrome = is_palindrome(s)

if palindrome == True:
    print (f"'{s}' is a palindrome!")
else:
    print (f"'{s}' is not a palindrome")