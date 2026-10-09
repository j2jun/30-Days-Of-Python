# Exercises: Day 12
# Write a function which generates a six digit/character random_user_id.
def random_user_id():
    import random
    import string
    
    # Generate a random string of 6 characters (letters and digits)
    characters = string.ascii_letters + string.digits
    random_id = ''.join(random.choice(characters) for _ in range(6))
    
    return random_id

def user_id_gen_by_user():
    import random
    import string
    
    # Get user input for the number of characters and IDs
    num_chars = int(input("Enter the number of characters for the user ID: "))
    num_ids = int(input("Enter the number of user IDs to generate: "))
    
    # Generate the specified number of random user IDs
    user_ids = []
    characters = string.ascii_letters + string.digits
    for _ in range(num_ids):
        random_id = ''.join(random.choice(characters) for _ in range(num_chars))
        user_ids.append(random_id)
    
    return user_ids

def rgb_color_gen():
    import random
    
    # Generate a random RGB color
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    return (r, g, b)

# Level 2
def list_of_hexa_colors(num_colors):
    import random
    
    hexa_colors = []
    for _ in range(num_colors):
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        hexa_colors.append(color)
    
    return hexa_colors

def list_of_rgb_colors(num_colors):
    import random
    
    rgb_colors = []
    for _ in range(num_colors):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        rgb_colors.append(color)
    
    return rgb_colors

def generate_colors(color_type, num_colors):
    if color_type == 'hexa':
        return list_of_hexa_colors(num_colors)
    elif color_type == 'rgb':
        return list_of_rgb_colors(num_colors)
    else:
        raise ValueError("Invalid color type. Choose 'hexa' or 'rgb'.")

# Level 3
def shuffle_list(input_list):
    import random
    
    # Shuffle the input list
    shuffled_list = input_list[:]
    random.shuffle(shuffled_list)
    
    return shuffled_list

def factorial(num):
    if num < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif num == 0 or num == 1:
        return 1
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result

