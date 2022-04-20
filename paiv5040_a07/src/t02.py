"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Lucas Paiva-Bernard
ID:      210985040
Email:   paiv5040@mylaurier.ca
__updated__ = "2022-03-10"
-------------------------------------------------------
"""
# Imports
from Sorted_List_linked import Sorted_List

# Code

print ("---------------------")
print ("Clean:")
source = Sorted_List()
source.insert(5)
source.insert(5)
source.insert(5)
source.clean()
for i in source:
    print (i)
print ("---------------------")
print ("Count:")
source1 = Sorted_List()
source2 = Sorted_List()
target = Sorted_List()
key = 3
source1.insert(1)
source1.insert(2)
source1.insert(3)
source2.insert(1)
source2.insert(2)
source2.insert(3)

print (source1.count(key))
print ("---------------------")
print ("Insert:")

source1.insert(99)

for i in source1:
    print (i)

print ("---------------------")
print ("Index:")

print (source1.index(99))


print ("---------------------")
print ("Find:")

print (source1.find(99))

print ("---------------------")
print ("Intersection:")
target = Sorted_List()
source1.insert(1)
source1.insert(2)
source1.insert(3)
source2.insert(1)
source2.insert(2)
source2.insert(3)

target.intersection(source1, source2)
for i in target:
    print (i)
print ("---------------------")
print ("Is_identical:")

x = source1.is_identical(source2)

print (x)
print ("---------------------")
print ("Max:")

print (source1.max())

print ("---------------------")
print ("Min:")

print (source1.min())
print ("---------------------")
print ("Peek:")

print (source1.peek())

print ("---------------------")
print ("Remove:")
key = 1
source1.remove(key)
for i in source1:
    print (i)

print ("---------------------")
print ("remove_front:")
source1.insert(1)
source1.remove_front()

for i in source1:
    print (i)

print ("---------------------")
print ("Union:")

target = Sorted_List()
target1 = Sorted_List()
target2 = Sorted_List()
target2.insert(3)
target1.insert(1)
target2.insert(2)
target1.insert(2)
target2.insert(4)
target1.insert(5)
target.union(target1, target2)

for i in target:
    print (i)

print ("---------------------")


