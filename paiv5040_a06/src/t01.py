"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Lucas Paiva-Bernard
ID:      210985040
Email:   paiv5040@mylaurier.ca
__updated__ = "2022-03-02"
-------------------------------------------------------
"""
# Imports
from Queue_linked import Queue

# Code
queue = Queue()
print ("Is empty:")
print (queue.is_empty())

print ("------------------------")
print ("Insert 5:")
queue.insert(5)
for i in queue:
    print (i)

print ("------------------------")
print ("Combine:")

queue1 = Queue()
queue2 = Queue()
queue3 = Queue()

queue1.insert(1)
queue2.insert(2)
queue3.insert(3)

queue1.combine(queue2, queue3)

for i in queue1:
    print (i)
    
print ("------------------------")
print ("Peek:")

print (queue1.peek())

print ("------------------------")
print ("Remove: ")
print (queue1.remove())

print ("------------------------")
print ("Is Identical:")

print (queue1.is_identical(queue2))

print ("------------------------")
print ("Length: ")

print (len(queue1))

print ("------------------------")
print ("Split alt:")

target1, target2 = queue1.split_alt()
print ("---------")
print ("Target1: ")
for i in target1:
    print (i)
print ("---------")
print ("Target2: ")

for i in target2:
    print (i)
    

