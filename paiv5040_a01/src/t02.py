"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Lucas Paiva-Bernard
ID:      210985040
Email:   paiv5040@mylaurier.ca
__updated__ = "2022-01-09"
-------------------------------------------------------
"""
# Imports
from functions import dsmvwl

# Code

s = str(input("Enter a string: "))

out = dsmvwl(s)

print (f"Sentence: {s}")
print (f"Disemvowelled: {out}")
