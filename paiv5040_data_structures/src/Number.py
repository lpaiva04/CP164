"""
-------------------------------------------------------
A simple number class.
-------------------------------------------------------
Author:  Lucas Paiva-Bernard
ID:      210985040
Email:   paiv5040@mylaurier.ca
__updated__ = "2022-03-26"
-------------------------------------------------------
"""


class Number:
    """
    -------------------------------------------------------
    Wraps a class definition around integers.
    Uses class attribute comparisons to determine how many times 
    comparison functions are called on the class.
    Use: print(Number.comparisons)
    Use: Number.comparisons = 0
    -------------------------------------------------------
    """
    comparisons = 0

    def __init__(self, value):
        """
        -------------------------------------------------------
        Creates a Number object.
        Use: target = Number(value)
        -------------------------------------------------------
        Parameters:
            value - an integer (int)
        Returns:
            A Number object (Number)
        -------------------------------------------------------
        """
        self._value = value
        return

    def __str__(self):
        """
        -------------------------------------------------------
        Creates a formatted string of Number.
        Use: string = str(source)
        Use: print(source)
        -------------------------------------------------------
        Returns:
            the formatted contents of _value (str)
        -------------------------------------------------------
        """
        return str(self._value)

    def __eq__(self, target):
        """
        -------------------------------------------------------
        Compares this Number against another Number for equality.
        Use: source == target
        -------------------------------------------------------
        Parameters:
            target - Number to compare to (Number)
        Returns:
            result - True if _values match, False otherwise (boolean)
        -------------------------------------------------------
        """
        Number.comparisons += 1
        result = self._value == target._value
        return result

    def __lt__(self, target):
        """
        -------------------------------------------------------
        Determines if this Number comes before another.
        Use: source < target
        -------------------------------------------------------
        Parameters:
            target - Number to compare to (Number)
        Returns:
            result - True if source precedes target,
                False otherwise (boolean)
        -------------------------------------------------------
        """
        Number.comparisons += 1
        result = self._value < target._value
        return result

    def __le__(self, target):
        """
        -------------------------------------------------------
        Determines if this Number precedes or is or equal to another.
        Use: source <= target
        -------------------------------------------------------
        Parameters:
            target - Number to compare to (Number)
        Returns:
            result - True if source precedes or is equal to target,
                False otherwise (boolean)
        -------------------------------------------------------
        """
        Number.comparisons += 1
        result = self._value <= target._value
        return result