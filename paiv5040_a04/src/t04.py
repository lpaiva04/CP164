"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Lucas Paiva-Bernard
ID:      210985040
Email:   paiv5040@mylaurier.ca
__updated__ = "2022-02-01"
-------------------------------------------------------
"""
# Imports
from functions import pq_split_key
from Priority_Queue_array import Priority_Queue

# Code
source = Priority_Queue()
key = int(input("Enter the key: "))

for n in range(0,9):
    source.insert(n)
print (f"Key: {key}")
print ("Source:")
for i in source:
    print (i)
print ("-------------------")
target1, target2 = pq_split_key(source, key)

print ("Target 1:")
for i in target1:
    print (i)
print ("-------------------")
print ("Target 2:")
for i in target2:
    print (i)