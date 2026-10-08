empty_list = list()  # this is an empty list, no item in the list
print(len(empty_list))  # 0

# list of fruits
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage',
              'Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter',
                   'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React', 'Redux',
             'Node', 'MongDB']  # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# Print the lists and it length
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:', animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Number of countries:', len(countries))

# Modifying list

fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0]  # we are accessing the first item using its index
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange
last_fruit = fruits[3]
print(last_fruit)  # lemon
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

# Accessing itmes
fruits = ['banana', 'orange', 'mango', 'lemon']
last_fruit = fruits[-1]
second_last = fruits[-2]
print(last_fruit)       # lemon
print(second_last)      # mango

# Slicing items
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4]  # it returns all the fruits
# this is also give the same result as the above
all_fruits = fruits[0:]  # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3]  # it does not include the end index
orange_mango_lemon = fruits[1:]

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:]  # it returns all the fruits
# this is also give the same result as the above
orange_and_mango = fruits[-3:-1]  # it does not include the end index
orange_mango_lemon = fruits[-3:]


fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'Avocado'
print(fruits)  # ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)  # ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)  # ['avocado', 'apple', 'mango', 'lime']

# checking items
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False

# Append
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
# ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime]
fruits.append('lime')
print(fruits)

# insert
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple')  # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
# ['banana', 'orange', 'apple', 'mango', 'lime','lemon',]
fruits.insert(3, 'lime')
print(fruits)

# remove
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon']
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango']

# pop
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(0)
print(fruits)       # ['orange', 'mango']

# del
fruits = ['banana', 'orange', 'mango', 'lemon']
del fruits[0]
print(fruits)       # ['orange', 'mango', 'lemon']

del fruits[1]
print(fruits)       # ['orange', 'lemon']
del fruits
# print(fruits)       # This should give: NameError: name 'fruits' is not defined

# clear
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)       # []

# copying a lits

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']

# join
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]
integers = negative_numbers + zero + positive_numbers
print(integers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

# join with extend
num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1)
negative_numbers = [-5, -4, -3, -2, -1]
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits)

# count
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3

# index
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))
# Reverse
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages)

# sort
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
ages.sort(reverse=True)
print(ages)


# Excercises: Day 5
lst1 = []
lst2 = list()

lst1 = [1, 2, 3, 4, 5]
print(lst1)  # [1, 2, 3, 4, 5]

print(len(lst1))  # 5

print(lst1[0])  # 1
print(lst1[2])  # 3
print(lst1[4])  # 5

mixed_data_types = ['JJ', 30, 76, 'Single', 'USA']

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print(mixed_data_types)
print(it_companies)

print(len(it_companies))  # 7

print(it_companies[0])  # Facebook
print(it_companies[3])  # Apple
print(it_companies[-1])  # Amazon

it_companies[0] = 'Meta'
print(it_companies)  # ['Meta', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

it_companies.append('Twitter')
print(it_companies)  # ['Meta', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Twitter']

it_companies.insert(3, 'Tesla')
print(it_companies)  # ['Meta', 'Google', 'Microsoft', 'Tesla', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Twitter']

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()
print(it_companies)  # ['Meta', 'GOOGLE', 'Microsoft', 'Tesla', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Twitter']

print('#; '.join(it_companies))

print('Facebook' in it_companies)  # False

it_companies.sort()
print(it_companies)  # ['Amazon', 'Apple', 'GOOGLE', 'IBM', 'Meta', 'Microsoft', 'Oracle', 'Tesla', 'Twitter']

it_companies.sort(reverse=True)
print(it_companies)  # ['Twitter', 'Tesla', 'Oracle', 'Microsoft', 'Meta', 'IBM', 'GOOGLE', 'Apple', 'Amazon']

first_three = it_companies[:3]
print(first_three)  # ['Twitter', 'Tesla', 'Oracle']

last_three = it_companies[-3:]
print(last_three)  # ['IBM', 'GOOGLE', 'Apple', 'Amazon']

middle_companies = it_companies[len(it_companies) // 2 - 1:len(it_companies) // 2 + 2]
print(middle_companies)  # ['Meta', 'IBM', 'GOOGLE']

it_companies.pop(0)
print(it_companies)  # ['Tesla', 'Oracle', 'Microsoft', 'Meta', 'IBM', 'GOOGLE', 'Apple', 'Amazon']

it_companies.pop(len(it_companies) // 2)
print(it_companies)  # ['Tesla', 'Oracle', 'Meta', 'IBM', 'GOOGLE', 'Apple', 'Amazon']

it_companies.pop(-1)
print(it_companies)  # ['Tesla', 'Oracle', 'Meta', 'IBM', 'GOOGLE', 'Apple']

it_companies.clear()
print(it_companies)  # []

del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end
print(full_stack)

full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)  # ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Python', 'SQL', 'Node', 'Express', 'MongoDB']

# Level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print(f"Min age: {ages[0]}")
print(f"Max age: {ages[-1]}")
print(f"Range of ages: {ages[-1] - ages[0]}")

ages.append(29)
ages.insert(0, 17)
print(ages)

median_age = (ages[len(ages) // 2 - 1] + ages[len(ages) // 2]) / 2
print(f"Median age: {median_age}")

average_age = sum(ages) / len(ages)
print(f"Average age: {average_age}")

range_of_ages = ages[-1] - ages[0]
print(f"Range of ages: {range_of_ages}")

# Compare the value of (min - average) and (max - average), use abs() method
min_diff = abs(ages[0] - average_age)
max_diff = abs(ages[-1] - average_age)
print(f"Absolute difference between min and average: {min_diff}")
print(f"Absolute difference between max and average: {max_diff}")

'''
1) find the middle country(ies) in the countries list
2) Divide the countries list into two equal lists if it is even if not one more country for the first half.
3) ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
'''
middle_index = len(countries) // 2
if len(countries) % 2 == 0:
    middle_countries = countries[middle_index - 1:middle_index + 1]
else:
    middle_countries = countries[middle_index:middle_index + 1]
print(f"Middle country(ies): {middle_countries}")

first_half = countries[:middle_index + len(countries) % 2]
second_half = countries[middle_index + len(countries) % 2:]
print(f"First half: {first_half}")
print(f"Second half: {second_half}")
