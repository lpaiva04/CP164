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
from Queue_circular import Queue

# Code

queue = Queue()

print (f"Is empty: {queue.is_empty()}")
print (f"Is full: {queue.is_full()}")
print ("Insert 5 twice:")
queue.insert(5)
queue.insert(5)
print (f"Length: {len(queue)}")
print (f"peek: {queue.peek()}")
print ("Remove front:")
queue.remove()
print (f"New length after removing: {len(queue)}")


