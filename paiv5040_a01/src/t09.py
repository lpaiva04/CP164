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
from functions import pig_latin

# Code

word = str(input("Enter a word: "))

pl = pig_latin(word)

print (f"Pig Latin word: {pl}")