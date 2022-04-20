"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Lucas Paiva-Bernard
ID:      210985040
Email:   paiv5040@mylaurier.ca
__updated__ = "2022-01-27"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from functions import reroute
# Code

values_in = [1, 2, 3, 4, 5, 6, 7, 8, 9]
opstring = "SSXXSXSSSSXX"

values_out = reroute(opstring, values_in)
print (f"Opstring: {opstring}")
print (f"Original list: {values_in}")
print (f"Reordered Version: {values_out}")