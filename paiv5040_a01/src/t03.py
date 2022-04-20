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
from functions import file_analyze

# Code

fv = open("fruits", "r")

u, l, d, w, r = file_analyze(fv)

fv.close()

print (f"Uppercase letters: {u}")
print (f"Lowercase letters: {l}")
print (f"Digits: {d}")
print (f"Whitespace characters: {w}")
print (f"Other characters: {r}")
