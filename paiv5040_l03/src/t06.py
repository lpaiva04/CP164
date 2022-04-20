"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Lucas Paiva-Bernard
ID:      210985040
Email:   paiv5040@mylaurier.ca
__updated__ = "2022-01-30"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue
from utilities import array_to_pq, pq_to_array, priority_queue_test

# Code
food = open("foods.txt", "r")
pq = Priority_Queue()
source = [food.readline(), food.readline(), food.readline(), food.readline(), food.readline()]
print ("Array to pq: ")
array_to_pq(pq, source)
for i in pq:
    print (i)
print ("pq to array:")
pq = Priority_Queue()
for i in range(0, 5):
    pq.insert(food.readline())
target = []

pq_to_array(pq, target)

print (target)
    
print ("Priority Queue Tests:")

a = [food.readline(), food.readline(), food.readline(), food.readline(), food.readline()]

print(priority_queue_test(a))
