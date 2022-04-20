"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Lucas Paiva-Bernard
ID:      210985040
Email:   paiv5040@mylaurier.ca
__updated__ = "2022-03-18"
-------------------------------------------------------
"""
# Imports:
from functions import comparison_total, do_comparisons
from BST_linked import BST
from Letter import Letter

# Code:
bst1 = BST()
bst2 = BST()
bst3 = BST()
fh = open('gibbon.txt', 'r')
DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

for data in DATA1:
    letter = Letter(data)
    bst1.insert(letter)
for data in DATA2:
    letter = Letter(data)
    bst2.insert(letter)
for data in DATA3:
    letter = Letter(data)
    bst3.insert(letter)

do_comparisons(fh, bst1)              
do_comparisons(fh, bst2)              
do_comparisons(fh, bst3)    

total1 = comparison_total(bst1)
total2 = comparison_total(bst2)
total3 = comparison_total(bst3)

print(f"Comparing by Order: ABCDEFGHIJKLMNOPQRSTUVWXYZ: {total1}")
print(f"Comparing by Order: MFTCJPWADHKNRUYBEIGLOQSVXZ: {total2}")
print(f"Comparing by Order: ETAOINSHRDLUCMPFYWGBVKJXZQ: {total3}")