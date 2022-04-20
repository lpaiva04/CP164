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
from Queue_array import Queue
from utilities import array_to_queue, queue_to_array, queue_test
# Code
queue = Queue()
source = [1, 2, 3, 4, 5]
print ("Array to queue: ")
array_to_queue(queue, source)
for i in queue:
    print (i)
print ("Queue to array:")
queue = Queue()
for i in range(0, 5):
    queue.insert(0)
target = []

queue_to_array(queue, target)

print (target)
    
print ("Queue Tests:")

a = [1, 2, 3, 4, 5]

print(queue_test(a))
