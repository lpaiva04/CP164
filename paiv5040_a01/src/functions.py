"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Lucas Paiva-Bernard
ID:      210985040
Email:   paiv5040@mylaurier.ca
__updated__ = "2022-01-09"
-------------------------------------------------------
"""
# Imports

# Constants

def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains
    only one copy of each of its integers. The order of values
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """
    cleaned = []
    element = 0
    n = 1
    
    while element < len(values):
        n = element + 1
        while n < len(values):
            if values[n] == values[element]:
                values.pop(n)
                n -= 1 
            n += 1
        element += 1              
    return 

def dsmvwl(s):
    """
    -------------------------------------------------------
    Disemvowels a string. out contains all the characters in s
    that are not vowels. ('y' is not considered a vowel.) Case is preserved.
    Use: out = dsmvl(s)
    -------------------------------------------------------
    Parameters:
       s - a string (str)
    Returns:
       out - s with the vowels removed (str)
    -------------------------------------------------------
    """
    out = ""
    vowels = "aeiouAEIOU"
    
    for letter in s:
        if letter not in vowels:
            out += letter
    return out
    
def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged.
    Use: u, l, d, w, r = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        u - the number of uppercase letters in the file (int)
        l - the number of lowercase letters in the file (int)
        d - the number of digits in the file (int)
        w - the number of whitespace characters in the file (int)
        r - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    u = 0
    l = 0
    d = 0
    w = 0
    r = 0
    line = fv.readline()
    
    while line != "":
        for i in line:
            if i.isupper():
                u += 1
            elif i.islower():
                l +=1
            elif i.isdigit():
                d += 1
            elif i.isspace():
                w += 1
            else:
                r += 1
        line = fv.readline()
   
    return u, l, d, w, r
    
def is_leap_year(year):
    """
    -------------------------------------------------------
    Leap year determination.
    Use: leap_year = is_leap_year(year)
    -------------------------------------------------------
    Parameters:
        year - year to determine if it is a leap year (int > 0)
    Returns:
        leap_year - True if year is a leap year, False otherwise (boolean)
    -------------------------------------------------------
    """
    leap_year = False
    
    if year % 4 == 0 and year % 100 != 0:
        leap_year = True
    if year % 100 == 0 and year % 400 == 0:
        leap_year = True
    
    return leap_year    
    
def is_palindrome(s):
    """
    -------------------------------------------------------
    Determines f s is a palindrome. Ignores case, spaces, and
    punctuation in s.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """
    punctuation = "!@#$%^&*()_+=|\}]{[:;<,>.?/"
    palindrome = True
    i = 0
    n = len(s) - 1
    while i < len(s) / 2 and palindrome == True:
        if s[i].isspace() or s[i] in punctuation:
            i += 1
        if s[n].isspace() or s[n] in punctuation:
            n -= 1
        if s[i].lower() != s[n].lower():
            palindrome = False
        i += 1
        n -= 1 
    return palindrome

def max_diff(a):
    """
    -------------------------------------------------------
    Returns maximum absolute difference between adjacent values in a list.
    a must be unchanged.
    Use: md = max_diff(a)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of int)
    Returns:
        md - the largest absolute difference between adjacent
            values in a list (int)
    -------------------------------------------------------
    """
    md = 0
    integer = 1
    while integer < len(a):
        if abs(a[integer - 1] - a[integer]) > md:
            md = abs(a[integer - 1] - a[integer])
        integer += 1    
    return md
        
def matrix_transpose(a):
    """
    -------------------------------------------------------
    Transpose the contents of matrix a.
    Use: b = matrix_transpose(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (list of lists of ?)
    Returns:
        b - the transposed matrix (list of lists of ?)
    -------------------------------------------------------
    """
    b = []
    
    for i in range(len(a[0])):
        b.append([])
        for n in range(len(a)):
            b[i].append(0)
    for i in range(len(a)):
        for n in range(len(a[0])):
            b[n][i] = a[i][n]
            
    return b

def matrix_stats(a):
    """
    -------------------------------------------------------
    Determines the smallest, largest, total, and average of
    the values in the 2D list a. You may assume there is at
    least one value in a.
    a must be unchanged.
    Use: small, large, total, average = matrix_stats(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list of numbers (2D list of float)
    Returns:
        small - the smallest number in a (float)
        large - the largest number in a (float)
        total - the total of all numbers in a (float)
        average - the average of all numbers in a (float)
    -------------------------------------------------------
    """
    small = 1000
    large = -1000
    total = 0
    count = 0
    
    for i in a:
        for j in i:
            count += 1
            if j <= small:
                small = j
            elif j >= large:
                large = j
            total += j
    average = total / count 
    
    return small, large, total, average
           
def pig_latin(word):
    """
    -------------------------------------------------------
    Converts a word to Pig Latin. The conversion is:
    - if a word begins with a vowel, add "way" to the end of the word.
    - if the word begins with consonants, move the leading consonants to
    the end of the word and add "ay" to the end of that.
    "y" is treated as a consonant if it is the first character in the word,
    and as a vowel for anywhere else in the word.
    Preserve the case of the word - i.e. if the first character of word
    is upper-case, then the new first character should also be upper case.
    Use: pl = pig_latin(word)
    -------------------------------------------------------
    Parameters:
        word - a string to convert to Pig Latin (str)
    Returns:
        pl - the Pig Latin version of word (str)
    ------------------------------------------------------
    """
    ending = ""
    i = 0
    pl = ""
    vowels = "aeiouAEIOU"
    
    if word[0] in vowels:
        word += "way"
        pl = word
    else:
        while word[i] not in vowels:
            ending += word[i].lower()
            i += 1
        pl += word[i].upper()    
        pl += word[i+1:1000]
        pl += ending
        pl += "ay"
        
    return pl
    
    
    
    
    
    
    
    
    
    
    
        
    