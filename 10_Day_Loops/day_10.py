# Exercises: Day 10
for i in range(0, 10):
    print(i, end=' ')
print()

count = 0
while count < 10:
    print(count, end=' ')
    count += 1
print()

for i in range(10, 0, -1):
    print(i, end=' ')
print()

count = 10
while count > 0:
    print(count, end=' ')
    count -= 1
print()

for i in range(1, 7):
    print(i * '#')
print()

count = 1
while count <= 6:
    print(count * '#')
    count += 1
print()

# Use nested loops to create
for i in range(1, 8):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

for i in range(0, 11):
    print('{} x {} = {}'.format(i, i, i * i))
print()

lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in lst:
    print(i, end=' ')
print()

for i in range(0, 101, 2):
    print(i, end=' ')
print()

for j in range(1, 101, 2):
    print(j, end=' ')
print()

# Level 2
count = 0
for i in range(0, 101):
    count += i
print('The sum of all numbers from 0 to 100 is:', count)

even_count = 0
odd_count = 0
for i in range(0, 101):
    if i % 2 == 0:
        even_count += i
    else:
        odd_count += i
print('The sum of all even numbers from 0 to 100 is:', even_count)
print('The sum of all odd numbers from 0 to 100 is:', odd_count)

# Level 3
# Go to the data folder and use the countries.py file (/Users/jjun/Code/learning/30-Days-Of-Python/data/countries.py). Loop through the countries and extract all the countries containing the word land.
import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).parent.parent))  # repo root, where data/ lives
import data.countries as countries
countries_with_land = []
for country in countries.countries:
    if 'land' in country:
        countries_with_land.append(country)
print('Countries containing the word "land":', countries_with_land)

fruit = ['banana', 'orange', 'mango', 'lemon']
for f in range(len(fruit)-1, -1, -1):
    print(fruit[f], end=' ')
print()

'''
Go to the data folder and use the countries_data.py file (/Users/jjun/Code/learning/30-Days-Of-Python/data/countries-data.py)
1. What are the total number of languages in the data
2. Find the ten most spoken languages from the data
3. Find the 10 most populated countries in the world
'''
from data.countries_data import countries_data
# 1. What are the total number of languages in the data
languages = set()
for country in countries_data:
    for language in country['languages']:
        languages.add(language)
print('Total number of languages in the data:', len(languages))

# 2. Find the ten most spoken languages from the data
from collections import Counter
language_counter = Counter()
for country in countries_data:
    for language in country['languages']:
        language_counter[language] += 1
most_spoken_languages = language_counter.most_common(10)
print('Ten most spoken languages from the data:')
for language, count in most_spoken_languages:
    print(f'{language}: {count}')

# 3. Find the 10 most populated countries in the world
population_counter = Counter()
for country in countries_data:
    population_counter[country['name']] = country['population']
most_populated_countries = population_counter.most_common(10)
print('Ten most populated countries in the world:')
for country, population in most_populated_countries:
    print(f'{country}: {population}')
    