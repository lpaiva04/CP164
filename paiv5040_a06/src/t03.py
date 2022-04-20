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
from Deque_linked import Deque

# Code
print ("Insert 1,2,3 into front and rear of two deques:")
deque1 = Deque()
deque2 = Deque()

deque1.insert_front(1)
deque1.insert_rear(2)
deque1.insert_front(3)
deque2.insert_front(1)
deque2.insert_rear(2)
deque2.insert_front(3)

for i in deque1:
    print (i)
print ("-----------")
for i in deque2:
    print (i)

print ("-----------------------")
print ("Peek:")

print (deque1.peek_front())
print (deque2.peek_rear())

print ("-----------------------")
print ("Remove:")

deque1.remove_front()
deque1.remove_rear()
deque2.remove_front()
deque2.remove_rear()
print ("-----------------------")
print ("Is Empty:")

print (deque1.is_empty())
print ("----------")
print (deque2.is_empty())

print ("-----------------------")
print ("Length:")

print (len(deque1))
print (len(deque2))

print ("-----------------------")

print ("Swap: ")
def print_deque(d):

    for v in d:
        print(v, end=", ")
    print()
    print("-" * 40)
    return

print("Original Deque")
d = Deque()
values = [1, 2, 3, 4, 5]

for v in values:
    d.insert_rear(v)
print_deque(d)
print("Swap same node")
# Make l and r point to the same node, second from the front
l = d._front._next
r = d._front._next
d._swap(l, r)
print_deque(d)
print("Swap front and rear nodes")
# make l and r point to the front and rear nodes
l = d._front
r = d._rear
d._swap(l, r)
print_deque(d)
print("Swap front and not rear")
# l points to front, r points to second from rear
l = d._front
r = d._rear._prev
d._swap(l, r)
print_deque(d)