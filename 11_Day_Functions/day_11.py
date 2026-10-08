# Exercises: Day 11
def add_two_numbers(num1, num2):
    return num1 + num2

def area_of_circle(radius):
    pi = 3.14
    return pi * radius ** 2

def convert_celsisus_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def check_season(month):
    if month in ['December', 'January', 'February']:
        return 'Winter'
    elif month in ['March', 'April', 'May']:
        return 'Spring'
    elif month in ['June', 'July', 'August']:
        return 'Summer'
    elif month in ['September', 'October', 'November']:
        return 'Autumn'
    else:
        return 'Invalid month'

def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return 'Slope is undefined (vertical line)'
    return (y2 - y1) / (x2 - x1)

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return 'No real roots'
    elif discriminant == 0:
        root = -b / (2*a)
        return (root,)
    else:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return (root1, root2)

def print_list(lst):
    for item in lst:
        print(item)

def reverse_list(lst):
    return lst[::-1]

def capitalize_list_items(lst):
    return [item.capitalize() for item in lst]

def add_item(lst, item):
    lst.append(item)
    return lst

def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

def sum_of_odds(lst):
    return sum(num for num in lst if num % 2 != 0)

def sum_of_evens(lst):
    return sum(num for num in lst if num % 2 == 0)

# Level 2
def evens_and_odds(lst):
    evens = sum(1 for num in lst if num % 2 == 0)
    odds = sum(1 for num in lst if num % 2 != 0)
    return {'evens': evens, 'odds': odds}

def factorial(n):
    if n < 0:
        return 'Factorial is not defined for negative numbers'
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def is_empty(lst):
    return len(lst) == 0

def calculate_mean(lst):
    if not lst:
        return 'List is empty'
    return sum(lst) / len(lst)

def calculate_median(lst):
    if not lst:
        return 'List is empty'
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

def calculate_mode(lst):
    if not lst:
        return 'List is empty'
    frequency = {}
    for item in lst:
        frequency[item] = frequency.get(item, 0) + 1
    max_freq = max(frequency.values())
    modes = [key for key, value in frequency.items() if value == max_freq]
    return modes

def calculate_range(lst):
    if not lst:
        return 'List is empty'
    return max(lst) - min(lst)

def calculate_variance(lst):
    if not lst:
        return 'List is empty'
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)

def calculate_std(lst):
    if not lst:
        return 'List is empty'
    variance = calculate_variance(lst)
    return variance ** 0.5

def greet(name):
    return f'Hello, {name}!'

def show_args(*args):
    return args 

# Level 3
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def unique_elements(lst):
    return list(set(lst))

# Write a function which checks if all the items of the list are of the same data type.
def are_all_same_type(lst):
    if not lst:
        return True
    first_type = type(lst[0])
    return all(isinstance(item, first_type) for item in lst)

def is_valid_variable_name(name):
    import keyword
    if not name.isidentifier() or keyword.iskeyword(name):
        return False
    return True

import countries_data as countries
'''
1) Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
2) Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
'''
def most_spoken_languages(countries, n=10):
    language_count = {}
    for country in countries:
        for language in country['languages']:
            language_count[language] = language_count.get(language, 0) + 1
    sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_languages[:n]

def most_populated_countries(countries, n=10):
    sorted_countries = sorted(countries, key=lambda x: x['population'], reverse=True)
    return [(country['name'], country['population']) for country in sorted_countries[:n]]

