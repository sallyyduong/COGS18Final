import random 
from my_module import functions


''' SMOOTHIE '''

# Dictionary with SMOOTHIE GREEN options and each item's calorie amount.
smoothie_green = {
    "kale" : 7,
    "spinach" : 37,
    "romaine" : 7,
}

# Randomly chooses a smoothie green. 
sm_green = random_key(smoothie_green)

# Finds the amount of calories for the randomly chosen smoothie green.
cal_sm_green = random_value(smoothie_green, sm_green)
       
    
# Dictionary with SMOOTHIE FRUIT options and each item's calorie amount.
smoothie_fruit = {
    "apricots" : 79,
    "blueberries": 84.4,
    "apples" : 65,
    "strawberry" : 48.6,
    "blackberry" : 61.9,
    "mango" : 107,
    "kiwi" : 108,
    "pineapple" : 82.5,
}

# Randomly chooses a smoothie fruit. 
sm_fruit = random_key(smoothie_fruit)

# Finds the amount of calories for the randomly chosen smoothie fruit.
cal_sm_fruit = random_value(smoothie_fruit, sm_fruit)


# Dictionary with SMOOTHIE LIQUID options and each item's calorie amount.
smoothie_liquid = {
    "water": 0,
    "dairy milk": 118,
    "almond milk" : 45.5,
    "soy milk" : 65.5,
    "orange juice": 56,
    "cranberry juice" : 58,
}

# Randomly chooses a smoothie liquid. 
sm_liquid = random_key(smoothie_liquid)

# Finds the amount of calories for the randomly chosen smoothie liquid.
cal_sm_liquid = random_value(smoothie_liquid, sm_liquid)
        
    
# Dictionary with SMOOTHIE PROTEIN options and each item's calorie amount.        
smoothie_protein = {
    "greek yogurt" : 29.5,
    "whole milk yogurt" : 30.5,
    "peanut butter" : 294.5,
    "almond butter" : 307,
    "protein powder" : 205.5,
    "flax seeds" : 267,
    "chia seeds" : 15,
    "walnut" : 309.5,
    "avocado" : 80
}

# Randomly chooses a smoothie protein. 
sm_protein = random_key(smoothie_protein)

# Finds the amount of calories for the randomly chosen smoothie protein.
cal_sm_protein = random_value(smoothie_protein, sm_protein)
     
    
# Adds the number of calories for smoothie green, fruit, liquid, and protein. 
sm_cal_total_num = cal_total_num(cal_sm_green, cal_sm_fruit, 
                                 cal_sm_liquid, cal_sm_protein) 
# Then, converts it to a string so it can be printed.      
sm_cal_total_str = cal_total_str(cal_sm_green, cal_sm_fruit, 
                                 cal_sm_liquid, cal_sm_protein) 


sm_serving = 1 # The original recipe makes 1 serving.

# Finds the amount of calories per serving by dividing total calories by recipe's servings.
sm_cal_total_serving = str(calories_divide(sm_cal_total_num, sm_serving))



''' STIR FRY '''

# Dictionary with STIR FRY BASE options and each item's calorie amount.
stirfry_base = {
    "white rice" : 408,
    "brown rice" : 432,
    "quinoa" : 367.8,
    "ramen noodle" : 280,
    "rice noodle" : 384,
    "egg noodles" : 292
}

# Randomly chooses a stir fry base. 
sf_base = random_key(stirfry_base)

# Finds the amount of calories for the randomly chosen stir fry base.
cal_sf_base = random_value(stirfry_base, sf_base)
 
              
# Dictionary with STIR FRY PROTEIN options and each item's calorie amount.
stirfry_protein = {
    "chicken" : 335,
    "tofu": 188,
    "garbanzo beans" : 364.5, 
    "salmon" : 233,
    "beef" : 339,
    "shrimp" : 209,
    "egg" : 365
}

# Randomly chooses a protein. 
sf_protein = random_key(stirfry_protein)

# Finds the amount of calories for the randomly chosen stir fry protein.
cal_sf_protein = random_value(stirfry_protein, sf_protein)
       
               
# Dictionary with STIR FRY VEGGIE options and each item's calorie amount.
stirfry_veggie = {
    "bok choy": 10,
    "cabbage" : 11,
    "broccoli": 15.5,
    "bell pepper" : 19,
    "mushroom" : 8,
    "zucchini": 10,
    "leek" : 27,
    "cauliflower" : 13.5,
    "brussel sprout" : 19
}


# Randomly chooses 2 different veggies (veggie 1 not that same as veggie 2).
# Finds the amount of calories for the randomly chosen veggies.

sf_veggie_1 = random_key(stirfry_veggie) # veggie 1

cal_sf_veggie_1 = random_value(stirfry_veggie, sf_veggie_1) # veggie 1 calories

sf_veggie_2 = random_key_2(stirfry_veggie, sf_veggie_1) #veggie 2

cal_sf_veggie_2 = random_value(stirfry_veggie, sf_veggie_2) #veggie 2 calories
        

# Dictionary with STIR FRY FRAGRANT options and each item's calorie amount.        
stirfry_fragrant = {
    "garlic" : 20,
    "red onion" : 12,
    "white onion" : 12
}

# Randomly chooses a fragrant. 
sf_frag = random_key(stirfry_fragrant)

# Finds the amount of calories for the randomly chosen stir fry protein.
cal_sf_frag = random_value(stirfry_fragrant, sf_frag)

        
# Dictionary with STIR FRY TOPPING options and each item's calorie amount.
stirfry_topping = {
    "sesame seed" : 104,
    "cilantro" : 1,
    "ginger" : 12,
    "green onion" : 4,
    "wonton strips" : 35
}

# Randomly chooses a topping. 
sf_top = random_key(stirfry_topping)

# Finds the amount of calories for the randomly chosen stir fry protein.
cal_sf_top = random_value(stirfry_topping, sf_top)


# Adds the number of calories of stir fry base, protein, vegetables, fragrant, and topping.  
sf_cal_total_num = cal_total_num(cal_sf_base, cal_sf_protein, cal_sf_veggie_1, 
                                 cal_sf_veggie_2, cal_sf_frag, cal_sf_top)

# Then, converts it to a string so it can be printed.
sf_cal_total_str = cal_total_str(cal_sf_base, cal_sf_protein, cal_sf_veggie_1, 
                                 cal_sf_veggie_2, cal_sf_frag, cal_sf_top)


sf_serving = 2 # The original recipe makes 2 servings.

# Finds the amount of calories per serving by dividing total calories by recipe's servings.
sf_cal_total_serving = str(calories_divide(sf_cal_total_num, sf_serving))
                       

    
''' OMELET '''  

# Dictionary with OMELET BASE options and each item's calorie amount.
omelet_base = {
    "eggs" : 468,
    "egg whites" : 102
}

# Randomly chooses a omelet base. 
om_base = random_key(omelet_base)

# Finds the amount of calories for the randomly chosen omelet base.
cal_om_base = random_value(omelet_base, om_base)
 

# Dictionary with OMELET INSIDES options and each item's calorie amount.
omelet_insides = {
    "ham" : 38,
    "bell pepper" : 6,
    "mushroom" : 12,
    "cheese" : 113,
    "cherry tomatoes" : 12,
    "onions" : 12,
    "beans" : 126,
    "spinach" : 28,
    "kale" : 33,
    "avocado" : 115
}

# Randomly chooses a omelet insides.
# Finds the amount of calories for the randomly chosen omelet insides.

om_insides_1 = random_key(omelet_insides) # inside item 1

cal_om_insides_1 = random_value(omelet_insides, om_insides_1) # inside item 1 calories

om_insides_2 = random_key_2(omelet_insides, om_insides_1) # inside item 2

cal_om_insides_2 = random_value(omelet_insides, om_insides_2) # inside item 2 calories

        
# Dictionary with OMELET TOPPINGS options and each item's calorie amount.
omelet_topping = {
    "green onion" : 4,
    "chives" : 2,
    "sour cream" : 46,
    "garlic" : 25,
    "salsa" : 100,
    "cheese" : 76,
    "cilantro" : 5
}

# Randomly chooses a omelet topping. 
# Finds the amount of calories for the randomly chosen omelet toppings.

om_top_1 = random_key(omelet_topping) # topping 1

cal_om_top_1 = random_value(omelet_topping, om_top_1) #topping 1 calories

om_top_2 = random_key_2(omelet_topping, om_top_1) # topping 2 

cal_om_top_2 = random_value(omelet_topping, om_top_2) #topping 2 calories
        
    
# Adds the number of calories of stir fry base, protein, vegetables, fragrant, and topping. 
om_cal_total_num = cal_total_num(cal_om_base, cal_om_insides_1, 
                                 cal_om_insides_2, cal_om_top_1, cal_om_top_2)

# Then, converts it to a string so it can be printed.        
om_cal_total_str = cal_total_str(cal_om_base, cal_om_insides_1, 
                                 cal_om_insides_2, cal_om_top_1, cal_om_top_2)


om_serving = 3 # The original recipe makes 3 servings.

#Finds the amount of calories per serving by dividing total calories by recipe's servings.
om_cal_total_serving = str(calories_divide(om_cal_total_num, om_serving))



''' FOOD GENERATOR/PRINTER ''' 

# Uses function food_randomizer to randomly select a food type from tuple food_types.
# Then, prints the result.
food_types = ("Smoothie", "Stir Fry", "Omelet")
your_food = food_randomizer(food_types)
print(your_food)


# Depending on the food type selected, the associated ingredients for that food type will be 
# printed along with its total calories and calories per serving.

if your_food == "Smoothie":
    
    # Prints the total number of calories.
    print("Total number of calories in this smoothie: " + sm_cal_total_str)
    
    # Prints the result of the total calories divided by the number of servings.
    # Prints calories per serving.
    print("This dish has 1 serving. Each serving is " + sm_cal_total_serving)
    
    #Prints the measurements (string) and randomized ingredients.
    print("1 cup of " + sm_green + ", 1 cup of " + sm_fruit + ", 1/2 cup of " 
          + sm_liquid + ", 3 tablespoons " + sm_protein)

elif your_food == "Stir Fry":
    
    # Prints the total number of calories.
    print("Total numbers of calories in this stir fry: " + sf_cal_total_str)
    
    # Prints the result of the total calories divided by the number of servings.
    # Prints calories per serving.
    print("This dish has 2 servings. Each serving is " + sf_cal_total_serving)
    
    #Prints the measurements (string) and randomized ingredients.    
    print("2 cups of " + sf_base + ", 1 cup of " + sf_protein + ", 1/2 cup of " 
          + sf_veggie_1 + ", 1/2 cup of " + sf_veggie_2 + ", 3 tablespoons of " 
          + sf_frag + ", 2 tablespoons of " + sf_top)

elif your_food == "Omelet": 
    
    # Prints the total number of calories.
    print("Total numbers of calories in this omelet: " + om_cal_total_str)
    
    # Prints the result of the total calories divided by the number of servings.
    # Prints calories per serving.
    print("This dish has 3 servings. Each serving is " + om_cal_total_serving)
    
    #Prints the measurements (string) and randomized ingredients.
    print("6 " + om_base + ", 3 tablespoons of " + om_insides_1 + ", 3 tablespoons of " 
          + om_insides_2 + ", 1 tablespoons of " + om_top_1 + ", 1 tablespoons of " 
          + om_top_2)
    
else:
    
    # Prints "Error", indicating a problem with the code.
    print("Error! Oh no!")

