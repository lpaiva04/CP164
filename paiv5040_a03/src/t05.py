"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Lucas Paiva-Bernard
ID:      210985040
Email:   paiv5040@mylaurier.ca
__updated__ = "2022-01-27"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from functions import is_palindrome_stack

# Code

stack = Stack()
string = str(input("Enter the string: "))
        
palindrome = is_palindrome_stack(string)

print (palindrome)