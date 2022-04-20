"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Lucas Paiva-Bernard
ID:      210985040
Email:   paiv5040@mylaurier.ca
__updated__ = "2022-03-24"
-------------------------------------------------------
"""
# Imports
from functions import comparison_total, insert_words
from Hash_Set_BST import Hash_Set

# Code
fv = open("otoos610.txt", "r")
hs = Hash_Set(20)
insert_words(fv, hs)

total, max_word = comparison_total(hs)

print ("Using linked BST Hash_set")
print ("")
print (f"Total Comparisons: {total}")
print (f"Word with maximum comparisons: {max_word}")