"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Lucas Paiva-Bernard
ID:      210985040
Email:   paiv5040@mylaurier.ca
__updated__ = "2022-03-05"
-------------------------------------------------------
"""
# Imports
from List_linked import List

# Code

list1 = List()
even = List()
odd = List()

list1.append(1)
list1.append(2)
list1.append(3)

list1.append(1)
list1.append(2)
list1.append(3)

even, odd = list1.split_alt_r()

for i in even:
    print (i)
print ("--------------")
for i in odd:
    print(i)