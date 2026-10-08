# Exercises: Day 6

from typing import Unpack


tpl1 = ()
tpl2 = tuple()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ('Alice', 'Bob', 'Charlie')  # Example names
brothers = ('David', 'Eve', 'Frank')   # Example names

# Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers

# How many siblings do you have?
print(f"Number of siblings: {len(siblings)}")

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ('John', 'Jane')  # Example names
print(f"Family members: {family_members}")

# Exercises: Level 2
# Unpack siblings and parents from family_members
siblings_unpacked, parents_unpacked = family_members[:len(siblings)], family_members[len(siblings):]

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'broccoli', 'spinach')
animal_products = ('milk', 'eggs', 'meat')
food_stuff_tp = fruits + vegetables + animal_products

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_index = len(food_stuff_lt) // 2
if len(food_stuff_lt) % 2 == 0:
    middle_items = food_stuff_lt[middle_index - 1:middle_index + 1]
else:
    middle_items = [food_stuff_lt[middle_index]]

# Slice out the first three items and the last three items from food_stuff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]

# Delete the food_stuff_tp tuple completely
del food_stuff_tp
# Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
# Check if 'Estonia' is a nordic country
print('Estonia' in nordic_countries)  # False
# Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)  # True  

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

