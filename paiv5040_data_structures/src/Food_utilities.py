"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Lucas Paiva-Bernard
ID:      210985040
Email:   paiv5040@mylaurier.ca
__updated__ = "2022-01-14"
-------------------------------------------------------
"""
from Food import Food


def get_food():
    """
    -------------------------------------------------------
    Creates a food object by requesting data from a user.
    Use: f = get_food()
    -------------------------------------------------------
    Returns:
        food - a completed food object (Food).
    -------------------------------------------------------
    """
    name = input("Food Name: ")

    origin = int(input("Enter the foods origin (integer from 1-11): "))
    
    vegetarian = str(input("Is the food vegitarian(Y/N)?: "))
    if vegetarian == "Y":
        v = True
    else:
        v = False
    
    calories = int(input("Enter the amount of calories: "))
        
    food = Food(name, origin, v, calories)
    return food


def read_food(line):
    """
    -------------------------------------------------------
    Creates and returns a food object from a line of string data.
    Use: f = read_food(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of food data in the format
        name|origin|is_vegetarian|calories (str)
    Returns:
        food - contains the data from line (Food)
    -------------------------------------------------------
    """
    list = line.split("|")
    
    if list[2] == "True":
        list[2] = True
    else:
        list[2] = False
        
    food = Food(list[0], int(list[1]), list[2], int(list[3]))
    return food


def read_foods(file_variable):
    """
    -------------------------------------------------------
    Reads a file of food strings into a list of Food objects.
    Use: foods = read_foods(file_variable)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file)
    Returns:
        foods - a list of food objects (list of Food)
    -------------------------------------------------------
    """
    foods = []
    line = file_variable.readline()
    
    while line != "":
        food = read_food(line)
        foods.append(food)
        line = file_variable.readline()

    return foods


def write_foods(file_variable, foods):
    """
    -------------------------------------------------------
    Writes a list of food objects to a file.
    file_variable contains the objects in foods as strings in the format
          name|origin|is_vegetarian|calories
    foods is unchanged.
    Use: write_foods(file_variable, foods)
    -------------------------------------------------------
    Parameters:
        file_variable - an open file of food data (file)
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """
    new_file = open("new_foods.txt", "w")

    for i in foods:
        new_file.write(str(i))
        print ("\n") 
       
    return


def get_vegetarian(foods):
    """
    -------------------------------------------------------
    Creates a list of vegetarian foods.
    foods is unchanged.
    Use: v = get_vegetarian(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        veggies - Food objects from foods that are vegetarian (list of Food)
    -------------------------------------------------------
    """
    veggies = []
    
    for i in foods:
        if i.is_vegetarian == True:
            veggies.append(i)
     
    return veggies


def by_origin(foods, origin):
    """
    -------------------------------------------------------
    Creates a list of foods by origin.
    foods is unchanged.
    Use: v = by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - a food origin (int)
    Returns:
        origins - Food objects from foods that are of a particular origin (list of Food)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))
    origins = []
    
    for i in foods:
        if i.origin == origin:
            origins.append(i)
            
    return origins


def average_calories(foods):
    """
    -------------------------------------------------------
    Determines the average calories in a list of foods.
    foods is unchanged.
    Use: avg = average_calories(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        avg - average calories in all Food objects of foods (int)
    -------------------------------------------------------
    """
    n = 0
    total = 0
    for i in foods:
        total += i.calories
        n += 1
    avg = total // n   
    
    return avg


def calories_by_origin(foods, origin):
    """
    -------------------------------------------------------
    Determines the average calories in a list of foods.
    foods is unchanged.
    Use: a = calories_by_origin(foods, origin)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the Food objects to find (int)
    Returns:
        avg - average calories for all Foods of the requested origin (int)
    -------------------------------------------------------
    """
    assert origin in range(len(Food.ORIGIN))
    n = 0
    total = 0
    origins = by_origin(foods, origin)
    
    for i in origins:
        total += i.calories
        n += 1
    avg = total // n
    
    return avg


def food_table(foods):
    """
    -------------------------------------------------------
    Prints a formatted table of foods, sorted by name.
    foods is unchanged.
    Use: food_table(foods)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
    Returns:
        None
    -------------------------------------------------------
    """
    print ("Food                               Origin          Vegetarian    Calories")
    print ("---------------------------------- --------------- ------------- --------")
    for i in foods:
        if i.is_vegetarian == 0: 
            print (f"{i.name:<35s}{Food.ORIGIN[i.origin]:<16s}False{i.calories:>12d}")
        if i.is_vegetarian == 1: 
            print (f"{i.name:<35s}{Food.ORIGIN[i.origin]:<16s}True {i.calories:>12d}")
  
    return


def food_search(foods, origin, max_cals, is_veg):
    """
    -------------------------------------------------------
    Searches for foods that fit certain conditions.
    foods is unchanged.
    Use: results = food_search(foods, origin, max_cals, is_veg)
    -------------------------------------------------------
    Parameters:
        foods - a list of Food objects (list of Food)
        origin - the origin of the food; if -1, accept any origin (int)
        max_cals - the maximum calories for the food; if 0, accept any calories value (int)
        is_veg - whether the food is vegetarian or not; if False accept any food (boolean)
    Returns:
        result - a list of foods that fit the conditions (list of Food)
            foods parameter must be unchanged
    -------------------------------------------------------
    """
    assert origin in range(-1, len(Food.ORIGIN))
    result = []
    
    if is_veg == "Y":
        is_veg = True
    elif is_veg == "N":
        is_veg = "F"
    
    for i in foods:
        if i.origin == origin:
            if max_cals > i.calories:
                if is_veg == i.is_vegetarian:
                    result.append(i)
        elif i.origin == -1:
            if max_cals > i.calories:
                if is_veg == i.is_vegetarian:
                    result.append(i)

    return result
    
    
    
    
    
    
    
    
    
    