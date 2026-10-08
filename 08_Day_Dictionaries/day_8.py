# Exercises: Day 8
dog = {}

dog = {"name": "Buddy", "color": "brown", "breed": "Labrador", "legs": 4, "age": 5}

student = {"first_name": "John", "last_name": "Doe", "gender": "Male", "age": 20, "marital_status": "Single", "skills": ["Python", "JavaScript"], "country": "USA", "city": "New York", "address": {"street": "123 Main St", "zip_code": "10001"}}

print(len(student))

print(student["skills"])

student["skills"].append("HTML")
print(student["skills"])

lst_of_keys = list(student.keys())
print(lst_of_keys)

lst_of_values = list(student.values())
print(lst_of_values)

lst_of_items = list(student.items())
print(lst_of_items)

del student["marital_status"]

del student