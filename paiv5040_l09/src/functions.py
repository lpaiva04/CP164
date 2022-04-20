"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Lucas Paiva-Bernard
ID:      210985040
Email:   paiv5040@mylaurier.ca
__updated__ = "2022-03-19"
-------------------------------------------------------
"""
# Imports
from Food import Food
# Code

def hash_table(slots, values):
    """
    -------------------------------------------------------
    Print a hash table of a set of values. The format is:
Hash     Slot Key
-------- ---- --------------------
     695    2 Lasagna, 7
    1355    4 Butter Chicken, 2
    Do not create an actual Hash_Set.
    Use: hash_table(slots, values)
    -------------------------------------------------------
    Parameters:
       slots - the number of slots available (int > 0)
       values - the values to hash (list of ?)
    Returns:
       None
    -------------------------------------------------------
    """
    print ("Hash     Slot Key")
    print ("-------- ---- ---------------------")
    for i in values:
        value = hash(i)
        slot = value % slots
        key = Food(i.name, i.origin, None, None)
        print (f"{value}        {slot:^d}     {key}")
    
    return
    
    
    
    