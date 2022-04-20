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
from functions import recurse

# Code

x = int(input("Enter an integer: "))
y = int(input("Enter an integer: "))

ans = recurse(x, y)

print (ans)