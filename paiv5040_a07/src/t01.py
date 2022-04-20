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
from List_linked import List

# Code

print ("Append:")
source = List()
source.append(5)
for i in source:
    print (i)
print ("---------------------")
print ("Clean:")
source.append(5)
source.append(5)
source.append(5)
source.clean()
for i in source:
    print (i)
print ("---------------------")
print ("Combine:")
source1 = List()
source2 = List()
target = List()

source1.append(1)
source1.append(2)
source1.append(3)
source2.append(1)
source2.append(2)
source2.append(3)

#target.combine(source1, source2)

for i in target:
    print (i)
print ("---------------------")
print ("Intersection:")
target = List()
source1.append(1)
source1.append(2)
source1.append(3)
source2.append(1)
source2.append(2)
source2.append(3)

target.intersection(source1, source2)
for i in target:
    print (i)
print ("---------------------")
print ("Is_identical:")

x = source1.is_identical(source2)

print (x)

print ("---------------------")
print ("Prepend:")

source1.prepend(99)
for i in source1:
    print (i)

print ("---------------------")
print ("remove_front:")
source1.append(1)
source1.remove_front()

for i in source1:
    print (i)

print ("---------------------")
print ("remove_many:")
source1.append(1)
source1.append(2)
source1.append(3)
source1.remove_many(1)

for i in source1:
    print (i)
print ("---------------------")
print ("Split:")



print ("---------------------")
print ("Split_alt:")

list = List()
list.append("99")
list.append("1")
list.append("99")
list.append("1")
list.append("99")
list.append("1")

target1, target2 = list.split_alt()
for i in target1:
    print (i)
for i in target2:
    print (i)
    
print ("---------------------")
print ("Union:")

target = List()

target.union(target1, target2)

for i in target:
    print (i)

print ("---------------------")
