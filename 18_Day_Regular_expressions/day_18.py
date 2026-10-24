# Exercises: Day 18
import re
import collections

'''
What is the most frequent word in the following paragraph?
    paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.

    [
    (6, 'love'),
    (5, 'you'),
    (3, 'can'),
    (2, 'what'),
    (2, 'teaching'),
    (2, 'not'),
    (2, 'else'),
    (2, 'do'),
    (2, 'I'),
    (1, 'which'),
    (1, 'to'),
    (1, 'the'),
    (1, 'something'),
    (1, 'if'),
    (1, 'give'),
    (1, 'develop'),
    (1, 'capabilities'),
    (1, 'application'),
    (1, 'an'),
    (1, 'all'),
    (1, 'Python'),
    (1, 'If')
    ]
'''
txt = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

words = re.findall(r'\w+', txt)
print(words)

dic = {}
for i in words:
    dic[i] = dic.get(i, 0) + 1
print(dic)

pairs = [(count, word) for word, count in dic.items()]
sorted_pairs = sorted(pairs, reverse=True)
print(sorted_pairs)
print('Most frequent word:', sorted_pairs[0])

'''
The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.
'''
txt = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.'
points = re.findall(r'-?\d+', txt)
print(points)

lst = [int(i) for i in points]
print(lst)

farthest_distance = max(lst) - min(lst)
print(farthest_distance)

# Level 2
'''
Write a pattern which identifies if a string is a valid python variable
'''
def is_valid_variable(name):  # renamed from `str` so it doesn't shadow the built-in str()
    match = re.fullmatch(r'[a-zA-Z_]\w*', name)  # fullmatch: whole string must match (re.match accepted 'first-name' via 'first'); r'' avoids the \w escape warning
    return match is not None  # return a bool instead of printing it

print(is_valid_variable('first_name')) # True
print(is_valid_variable('first-name')) # False
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('firstname')) # True

# Level 3
'''
Clean the following text. After cleaning, count three most frequent words in the string.
'''

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(name):
    matches = re.sub(r'[^\w\s]', '', name)  # delete any char that is neither a word char nor whitespace
    return matches
print(clean_text(sentence))

def most_frequent_words(text):  # takes the cleaned text (a string), not a function
    words = re.findall(r'\w+', text)  # use the parameter, not the global `sentence` (which is still dirty)
    dic = {}
    for i in words:
        dic[i] = dic.get(i, 0) + 1
        
    pairs = [(count, word) for word, count in dic.items()]
    sorted_pairs = sorted(pairs, reverse=True)
    return sorted_pairs[:3]  # return the list itself, matching the expected output

cleaned_text = clean_text(sentence)  # store the result once, as in the md sample
print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]