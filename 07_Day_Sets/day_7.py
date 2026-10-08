# Exercises: Day 7
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Level 1
# 1. Find the length of the set it_companies
print(len(it_companies))

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['LinkedIn', 'Snapchat', 'TikTok'])

# 4. Remove one of the companies from the set it_companies
it_companies.remove('IBM')  # or it_companies.discard('IBM')

# 5. What is the difference between remove and discard
# The difference between remove and discard is that remove will raise a KeyError if the item does not exist in the set, while discard will not raise an error if the item is not found.

# Level 2
# 1. Join A and B
union_set = A.union(B)

# 2. Find A intersection B
intersection_set = A.intersection(B)

# 3. Is A subset of B
is_subset = A.issubset(B)

# 4. Are A and B disjoint sets
are_disjoint = A.isdisjoint(B)

# 5. Join A with B and B with A
A_union_B = A.union(B)
B_union_A = B.union(A)

# 6. What is the symmetric difference between A and B
symmetric_difference = A.symmetric_difference(B)

# 7. Delete the sets completely
del A
del B

# Level 3
# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print(f"Length of age list: {len(age)}")
print(f"Length of age set: {len(age_set)}")

# 2. Explain the difference between the following data types: string, list, tuple and set
# - String: A string is an immutable sequence of characters used to represent text. It is defined using single or double quotes.
# - List: A list is a mutable ordered collection of items that can contain elements of different data types. It is defined using square brackets [].
# - Tuple: A tuple is an immutable ordered collection of items that can contain elements of different data types. It is defined using parentheses ().
# - Set: A set is an unordered collection of unique items.

# 3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()
unique_words = set(words)
print(f"Number of unique words: {len(unique_words)}")
