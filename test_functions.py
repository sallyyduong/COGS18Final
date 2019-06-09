import random 

def test_serving_divide(serving_divide):
    
    """Tests for the `serving_divide` function."""
    
    assert callable(serving_divide)
    assert serving_divide(500, 2) == 250
    assert serving_divide(1000, 2) == 500

def test_food_randomizer():
    
    """Tests for the `food_randomizer` function."""
    
    assert callable(food_randomizer)
    assert food_randomizer(food_types) == str
    #Test if value returned is from the food_types dictionary
    assert food_randomizer(food_types) == "Smoothie" or "Stir Fry" or "Omelet"
    assert food_types == tuple
    
def test_random_key():
    
    """Tests for the `random_key` function."""
    
    assert callable(random_key)
    # Test if value returned is from the dictionary
    assert random_key(["a", "b", "c"]) == "a" or "b" or "c"
    assert isinstance(random_key(["a", "b", "c"]), str)
    
def test_random_key_2():
    
    """Test for the `random_key_2` function."""
    
    assert callable(random_key_2)
    # Tests to make sure items don't repeat 
    #("c" shouldnt be returned because it was the first item)
    assert random_key_2(["a", "b", "c"], "c") != "c"

def test_random_value():
    
    """Test for the `random_value` function."""

    assert callable(random_value)
    #Test if correct value is returned
    dict_test = {"hi": 2, "bye":1}
    var = "hi"
    assert random_value(dict_test, var) == 2
    
def test_cal_total_num():
    
    """Test for the `cal_total_num` function."""
    
    assert callable(cal_total_num)
    assert isinstance(cal_total_num(1, 2, 3, 4, 5), int)
    assert cal_total_num(1, 1, 1, 1, 1) == 5

def test_cal_total_str():
    
    """Test for the `cal_total_str` function."""
    
    assert callable(cal_total_str)
    assert isinstance(cal_total_num(1, 2, 3, 4, 5), str)
    assert cal_total_num(1, 1, 1, 1, 1) == "5"

    