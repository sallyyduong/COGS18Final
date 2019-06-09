import random

def food_randomizer(food_types):
    """Randomly chooses an item from tuple of food types.
   
    Parameters
    ----------
    food_types: tuple
        Tuple holding food types: smoothie, stir fry, and omelet.
    
    Returns
    -------
    your_food : string
        String with a randomly chosen food item.
    
    """
    
    # Tuple food_types.
    food_types = ("Smoothie", "Stir Fry", "Omelet")
    # Chooses random element in tuple food_types.
    your_food = random.choice(food_types)
    
    
    return your_food


def random_key(dictionary):
    """Randomly chooses a key from selected dictionary.
    
    Parameters
    ----------
    dictionary : dict
        Dictionary holding keys (ingredients) and values (calories).
          
    Returns
    -------
    output : str
        String of the random key selected from dictionary.
    """
    
    # Chooses random key from selected dictionary.
    output = random.choice(list(dictionary.keys()))
    
    
    return output


def random_key_2(dictionary, first_item):
    """Randomly chooses a second key from selected dictionary.
    Ensures that the first key is not the same as the second key.
    (The output of function random_key_2 is different from the output of function random_key.)
    
    Parameters
    ----------
    dictionary : dict
        Dictionary holding keys (ingredients) and values (calories).
    
    first_item : str
        String of the random key selected from dictionary.
          
    Returns
    -------
    second_item : str
        String of random key selected from dictionary that is different from the first.
    """
    
    # Chooses random key from selected dictionary.    
    second_item = random.choice(list(dictionary.keys()))
    
    
    # Keeps randomizing the item if it is the same as the first item.
    # Ensures that the two items are not the same.
    if first_item == second_item:
        new_item = random.choice(list(dictionary.keys()))
        second_item = new_item
            
            
    return second_item


def random_value(dictionary, associated_var):
    """Retrieves selected value associated with key from random_key function.
    
    Parameters
    ----------
    dictionary : dict
        Dictionary holding keys (ingredients) and values (calories). 
        
    associated_var: str
        String of random key selected from dictionary.
    
    Returns
    -------
    output : int
        Int that gives the associated calories for selected key.
        Returns the int value of the selected key.
    """
    
    
    # Retrieves the output for the random key value selected.
    for item in dictionary:
        key = item
        value = dictionary[item]
    
        # Assigns value as the output.
        if key == associated_var:
             output = value 
                
                
    return output


def cal_total_num(num1=0, num2=0, num3=0, num4=0, num5=0, num6=0):
    """Adds calories from all variables. 
    If a variable is not defined, it is 0 calories.
    
    Parameters
    ----------
    num1 : int 
        The first number, to be added. 
    num2 : int 
        The second number, to be added.
    num3 : int
        The third number, to be added.
    num4 : int
        The fourth number, to be added.
    num5 : int 
        The fifth number, to be added.
    num6 : int
        The sixth number, to be added.
    
    Returns
    -------
    output : int
        Total calories from additing all numbers.
    """
    
    # Adds all the variables.
    output = num1 + num2 + num3 + num4 + num5
    
    
    return output


def cal_total_str(num1 = 0, num2 = 0, num3 = 0, num4 = 0, num5 = 0, num6=0):
    """Adds calories from all variables and returns it in string format.
    
    Parameters
    ----------
    num1 : int 
        The first number, to be added. 
    num2 : int 
        The second number, to be added.
    num3 : int
        The third number, to be added.
    num4 : int
        The fourth number, to be added.
    num5 : int 
        The fifth number, to be added.
    num6 : int
        The sixth number, to be added.
        
    Returns
    -------
    output : str
        Total calories from additing all numbers in string format.
    """
    
    # Adds all variables and converts to string.
    output = str(num1 + num2 + num3 + num4 + num5)
    
    
    return output


def calories_divide(total_calories, recipe_servings):
    """Divides the total amount of calories by the recipe's number of servings.
    
    Parameters
    ----------
    total_calories : int
        Int, the total amount of calories in the randomly generated food type.
        
    recipe_servings: int
        Int, number of servings from the original recipe.
    
    Returns
    -------
    output : int
        Int that is the amount of calories per serving.
    """
    
    # Divides total calories by the number of servings to get calories per serving.
    output = total_calories/recipe_servings
    
    
    return output





