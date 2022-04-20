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
#Imports:
from Letter import Letter

def do_comparisons(file_variable, bst):
    """
    -------------------------------------------------------
    Retrieves every letter in file_variable from bst. Generates
    comparisons in bst objects. Each Letter object in bst contains
    the number of comparisons found by searching for that Letter
    object in file_variable.
    Use: do_comparisons(file_variable, bst)
    -------------------------------------------------------
    Parameters:
        file_variable - the already open file containing data to evaluate (file)
        bst - the binary search tree containing 26 Letter objects
            to retrieve data from (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    # Zeroes out all comparison values in tree nodes
    for node in bst:
        node.comparisons = 0
        
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    file_variable.seek(0)
    file = file_variable.readlines()
    for line in file:
        for word in line:
            for letter in word:
                upper_letter = letter.upper()
                if upper_letter in ALPHABET:
                    key = Letter(upper_letter)
                    value = bst.retrieve(key)
    return

def comparison_total(bst):
    """
    -------------------------------------------------------
    Sums the comparison values of all Letter objects in bst.
    Use: total = comparison_total(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        total - the total of all comparison fields in the bst
            Letter objects (int)
    -------------------------------------------------------
    """
    total = 0
    for letter in bst.inorder():
        total += letter.comparisons
    return total

def letter_table(bst):
    """
    -------------------------------------------------------
    Prints a table of letter counts for each Letter object in bst.
    Use: letter_table(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    total = comparison_total(bst)
    print("Letter Count/Percent Table")
    print ("")
    print (f"Total Count: {total}")
    print ("")
    print ("Letter  Count       %")
    print ("-----------------------------------")
    for letter in bst.inorder():
        percent = (letter.count / total) * 100
        print(f"{letter.letter:<9s} {letter.count:>8d} {percent:^8.2f}")