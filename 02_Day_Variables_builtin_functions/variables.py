# Day 2: 30 Days of python programming
# Variables in Python

first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname': 'Asabeneh',
    'lastname': 'Yetayeh',
    'country': 'Finland',
    'city': 'Helsinki'
}

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

firstName = "Joseph"
lastName = "Jun"
fullName = firstName + " " + lastName
country1 = "Korea"
city1 = "Seoul"
age1 = 32
year1 = 1994
is_married = False
is_true = True
is_light_on = True
# declare multiple variable in one line
firstName, lastName, fullName, country1, city1, age1, year1, is_married, is_true, is_light_on = "Joseph", "Jun", "Joseph Jun", "Korea", "Seoul", 32, 1994, False, True, True

type(firstName)
len(firstName)
len(lastName)
num_one , num_two = 5, 4
subtract = num_one - num_two
multiply = num_one * num_two
divide = num_one / num_two
modulus = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two
radius = 30
area_of_circle = 3.14 * radius ** 2
circumference_of_circle = 2 * 3.14 * radius
radius = input("Enter the radius of the circle: ")
radius = float(radius)
area_of_circle = 3.14 * radius ** 2
circumference_of_circle = 2 * 3.14 * radius
print("Area of the circle:", area_of_circle)
print("Circumference of the circle:", circumference_of_circle)
# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = input("Enter your age: ")
print("First name:", first_name)
print("Last name:", last_name)
print("Country:", country)
print("Age:", age)
help('keywords')