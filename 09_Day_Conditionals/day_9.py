# Exercises: Day 9
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    years_needed = 18 - age
    print("You need {} more years to learn to drive.".format(years_needed))

'''Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.
'''
my_age = 25
your_age = int(input("Enter your age: "))
if my_age > your_age:
    age_diff = my_age - your_age
    if age_diff == 1:
        print("I am 1 year older than you.")
    else:
        print("I am {} years older than you.".format(age_diff))
elif my_age < your_age:
    age_diff = your_age - my_age
    if age_diff == 1:
        print("You are 1 year older than me.")
    else:
        print("You are {} years older than me.".format(age_diff))
else:
    print("We are the same age.")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > num2:
    print("{} is greater than {}".format(num1, num2))
elif num1 < num2:
    print("{} is less than {}".format(num1, num2))
else:
    print("{} is equal to {}".format(num1, num2))

# Level 2
score = int(input("Enter your score: "))
if score >= 80:
    print("A")
elif score >= 70:
    print("B")
elif score >= 60:
    print("C")
elif score >= 50:
    print("D")
else:
    print("F")

'''Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer'''
month = input("Enter the month: ")
if month in ["September", "October", "November"]:
    print("The season is Autumn.")
elif month in ["December", "January", "February"]:
    print("The season is Winter.")
elif month in ["March", "April", "May"]:
    print("The season is Spring.")
elif month in ["June", "July", "August"]:
    print("The season is Summer.")


fruits = ['banana', 'orange', 'mango', 'lemon']
'''If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')'''
fruit = input("Enter a fruit: ")
if fruit in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(fruit)
    print("Modified list:", fruits)

# Level 3
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

''' * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format:
'''
if person.get('is_married') and person.get('country') == 'Finland':
    print("{} {} lives in {}. He is married.".format(person.get('first_name'), person.get('last_name'), person.get('country')))
