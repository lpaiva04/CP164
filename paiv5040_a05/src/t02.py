"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Lucas Paiva-Bernard
ID:      210985040
Email:   paiv5040@mylaurier.ca
__updated__ = "2022-02-11"
-------------------------------------------------------
"""
# Imports
from Sorted_List_array import Sorted_List
from Food_utilities import read_food

# Code
file = open("foods.txt", "r")

food = read_food(file.readline())
source = Sorted_List()

for i in range(0, 3):
    source.insert(food)
    source.insert(read_food(file.readline()))
print ("-------------------------")
print ("clean:")
source.clean()

for i in source:
    print (i)


print ("-------------------------")
print ("find:")
key = (food)

print (source.find(key))



print ("-------------------------")
print ("index:")

key = (food)

print (source.index(key))

print ("-------------------------")
print ("intersection:")

source2 = Sorted_List()
for i in range(0, 3):
    source2.insert(food)
    source2.insert(read_food(file.readline()))

source1 = source2

target = Sorted_List()

target.intersection(source1, source2)

for i in target:
    print (i)
print ("-------------------------")
print ("is_identical:")

list = Sorted_List()
for i in range(1, 6):
    list.insert(read_food(file.readline()))
    
target = Sorted_List()
    
for i in range(0, 3):
    target.insert(food)
    target.insert(read_food(file.readline()))
print (list.is_identical(target))

target = list

print (list.is_identical(target))

print ("-------------------------")
print ("max:")

print (source.max())

print ("-------------------------")
print ("min:")

print (source.min())

print ("-------------------------")
print ("peek:")

print (source.peek())

print ("-------------------------")
print ("remove:")

print (source.remove(food))

print ("-------------------------")
print ("remove_front:")

print (source.remove_front())

print ("-------------------------")
print ("remove_many:")

key = food
source.insert(food)
source.insert(food)
source.insert(food)

for i in source:
    print (i)
print ("===============")
print (f"Remove all instances of key: {food}")
print ("===============")
source.remove_many(key)

for i in source:
    print (i)
print ("-------------------------")
print ("split:")
source.insert(read_food(file.readline()))
source.insert(read_food(file.readline()))
source.insert(read_food(file.readline()))

target1, target2 = source.split()

for i in target1:
    print (i)
print ("==================")
for i in target2:
    print (i)

print ("-------------------------")
print ("split_alt:")

target1, target2 = source.split_alt()

for i in target1:
    print (i)
print ("==================")
for i in target2:
    print (i)
print ("-------------------------")
print ("split_key:")

key = (food)
source.insert(food)
source.insert(food)
source.insert(food)
source.insert(read_food(file.readline()))
source.insert(read_food(file.readline()))
source.insert(read_food(file.readline()))

target1, target2 = source.split_key(key)

for i in target1:
    print (i)
print ("=================")
for i in target2:
    print (i)

print ("-------------------------")
print ("union:")

for i in range(0, 10):
    source1.insert(read_food(file.readline()))
for i in range(0, 10):
    source2.insert(food)
target = Sorted_List()

target.union(source1, source2)

for i in target:
    print(i)


