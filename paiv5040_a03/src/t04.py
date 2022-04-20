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

# Code
source = Stack()
n = 5

for i in range(n):
    value = int(input("Enter a value: "))
    source.push(value)
    
print ("-------------")
print ("Unreversed Stack:")
for i in source:
    print (i)
source.reverse()

print ("-------------")
print ("Reversed Stack:")
for i in source:
    print (i)