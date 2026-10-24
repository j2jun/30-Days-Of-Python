# Exercises: Level 1
import os
import json
import re
from collections import Counter

DATA = os.path.join(os.path.dirname(__file__), '..', 'data')

# 1. Count lines and words in a text file
def count_lines_and_words(path):
    with open(path) as f:
        text = f.read()
    return len(text.splitlines()), len(text.split())

for name in ['obama_speech.txt', 'michelle_obama_speech.txt',
             'donald_speech.txt', 'melina_trump_speech.txt']:
    lines, words = count_lines_and_words(os.path.join(DATA, name))
    print(f'{name}: {lines} lines, {words} words')


# 2. Find the most spoken languages
def most_spoken_languages(filename, n=10):
    with open(filename) as f:
        countries = json.load(f)
    languages = Counter(
        language for country in countries for language in country['languages']
    )
    ranked = sorted(languages.items(), key=lambda item: (item[1], item[0]), reverse=True)
    return [(count, language) for language, count in ranked[:n]]


print(most_spoken_languages(os.path.join(DATA, 'countries_data.json')))

# 3. Create a list of the ten most populated countries
def most_populated_countries(filename, n=10):
    with open(filename) as f:
        countries = json.load(f)
    ranked = sorted(countries, key=lambda country: country['population'], reverse=True)
    return [
        {'country': country['name'], 'population': country['population']} for country in ranked[:n]
    ]

print(most_populated_countries(os.path.join(DATA, 'countries_data.json')))

# Level 2
# 1. Extract all incoming email addresses
def extract_incoming_emails(filename):
    with open(filename) as f:
        return re.findall(r'^From (\S+@\S+)', f.read(), re.MULTILINE)

print(extract_incoming_emails(os.path.join(DATA, 'email_exchanges_big.txt')))

# 2. Find the most common words in the English language
def find_most_common_words(source, n):
    if os.path.isfile(source):
        with open(source) as f:
            source = f.read()
    words = re.findall(r"[a-zA-Z']+", source)
    return [(count, word) for word, count in Counter(words).most_common(n)]


print(find_most_common_words('the cat and the hat and the bat', 3))
print(find_most_common_words(os.path.join(DATA, 'obama_speech.txt'), 10))

# 3. find_most_frequents_words to find
for name in ['obama_speech.txt', 'michelle_obama_speech.txt',
             'donald_speech.txt', 'melina_trump_speech.txt']:
    print(name, find_most_common_words(os.path.join(DATA, name), 10))

# 4. Check text similarity
import sys
sys.path.insert(0, DATA)
from stop_words import stop_words


def clean_text(source):
    if os.path.isfile(source):
        with open(source) as f:
            source = f.read()
    return re.findall(r"[a-z']+", source.lower())


def remove_support_words(words):
    return [word for word in words if word not in stop_words]


def check_text_similarity(text1, text2):
    # Jaccard similarity: shared words / all distinct words
    words1 = set(remove_support_words(clean_text(text1)))
    words2 = set(remove_support_words(clean_text(text2)))
    return len(words1 & words2) / len(words1 | words2)


assert check_text_similarity('the cat sat', 'a cat sat') == 1.0
assert check_text_similarity('cat dog', 'cat bird') == 1 / 3
print(check_text_similarity(os.path.join(DATA, 'michelle_obama_speech.txt'),
                            os.path.join(DATA, 'melina_trump_speech.txt')))

# 5. Find the 10 most repeated words in romeo_and_juliet.txt
print(find_most_common_words(os.path.join(DATA, 'romeo_and_juliet.txt'), 10))

# 6. Count lines in hacker_news.csv mentioning Python, JavaScript and Java
with open(os.path.join(DATA, 'hacker_news.csv')) as f:
    lines = f.readlines()

print(sum(1 for line in lines if re.search(r'[Pp]ython', line)))
print(sum(1 for line in lines if re.search(r'[Jj]ava[Ss]cript', line)))
print(sum(1 for line in lines if 'Java' in line and not re.search(r'[Jj]ava[Ss]cript', line)))
