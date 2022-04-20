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
from List_array import List
from Food_utilities import read_food

# Code
file = open("foods.txt", "r")

food = read_food(file.readline())

print ("Clean:")
source = List()

for i in range(0, 3):
    source.append(food)
    source.append(read_food(file.readline()))

source.clean()
for i in source:
    print (i)
print ("--------------------------")
print ("Combine: ")
target = List()
source1 = [read_food(file.readline()), read_food(file.readline()),read_food(file.readline())]
source2 = [read_food(file.readline()), read_food(file.readline()),read_food(file.readline()), read_food(file.readline())]

target.combine(source1, source2)

for i in target:
    print (i)
print ("--------------------------")
print ("Intersection: ")

source2 = List()
for i in range(0, 3):
    source2.append(food)
    source2.append(read_food(file.readline()))

source1 = source2

target = List()

target.intersection(source1, source2)

for i in target:
    print (i)
print ("---------------------------")
print ("is_identical: ")

list = List()
for i in range(1, 6):
    list.append(read_food(file.readline()))
    
target = List()
    
for i in range(0, 3):
    target.append(food)
    target.append(read_food(file.readline()))
print (list.is_identical(target))

target = list

print (list.is_identical(target))

print ("----------------------------")
print ("prepend:")
source = List()
source.prepend(read_food(file.readline()))

for i in source:
    print (i)
print ("Prepend line:")    
source.prepend(read_food(file.readline()))

for i in source:
    print (i)
print ("----------------------------")
print ("remove_front:")

source.remove_front()

for i in source:
    print (i)


print ("----------------------------")
print ("remove_many:")

key = food
source.append(food)
source.append(food)
source.append(food)

for i in source:
    print (i)
print ("===============")
print (f"Remove all instances of key: {food}")
print ("===============")
source.remove_many(key)

for i in source:
    print (i)
print ("----------------------------")
print ("split:")
x = read_food(file.readline())
source.append(x)
source.append(x)
source.append(x)

target1, target2 = source.split()

for i in target1:
    print (i)
print ("=============================")
for i in target2:
    print (i)

print ("----------------------------")
print ("split_alt:")
source.append(read_food(file.readline()))
source.append(read_food(file.readline()))
for i in source:
    print (i)
print ("=================")
target1, target2 = source.split_alt()
for i in target1:
    print (i)
print ("=================")
for i in target2:
    print (i)


print ("----------------------------")
print ("union:")

source1 = List()
source2 = List()

for i in range(0, 3):
    source1.append(read_food(file.readline()))
for i in range(0, 3):
    source2.append(read_food(file.readline()))
    
list = List()

list.union(source1, source2)

for i in list:
    print (i)


















