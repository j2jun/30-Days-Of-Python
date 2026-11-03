# Exercises: Day 22
import requests
from bs4 import BeautifulSoup

# Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').
url = 'http://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)
status = response.status_code
print(status)
soup = BeautifulSoup(response.content, 'html.parser')
print(soup.title)
print(soup.title.get_text())
# print(soup.prettify())
import json
data = {
    'title': soup.title.get_text()
}
with open('data.json', 'w') as f:
    json.dump(data, f)
print("Data has been saved to data.json")

# Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file
# original 'https://archive.ics.uci.edu/ml/datasets.php' now 404s; the new page lists datasets as links, not a table
url = 'https://archive.ics.uci.edu/datasets'
response = requests.get(url)
response.raise_for_status()
soup = BeautifulSoup(response.content, 'html.parser')
data = [
    {'name': a.get_text(strip=True), 'url': 'https://archive.ics.uci.edu' + a['href']}
    for a in soup.select('a[href^="/dataset/"]')
    if a.get_text(strip=True)
]
with open('table_data.json', 'w') as f:
    json.dump(data, f)
print("Table data has been saved to table_data.json")

# Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). The table is not very structured and the scrapping may take very long time.
url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
# Wikipedia returns 403 for the default python-requests User-Agent, so identify the script
response = requests.get(url, headers={'User-Agent': '30DaysOfPython-exercise/1.0'})
response.raise_for_status()
soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table', {'class': 'wikitable'})

import re
def clean(cell):
    # turn <br> into spaces, drop footnote markers like [19] or [c], collapse whitespace, treat '–' as empty
    for br in cell.find_all('br'):
        br.replace_with(' ')
    text = ' '.join(re.sub(r'\[[^\]]*\]', '', cell.get_text()).split())
    return '' if text == '–' else text

# columns: 0 No., 1 portrait, 2 name, 3 term, 4 party color, 5 party, 6 election, 7 vice president
presidents = []
spans = {}  # column -> rows still covered by a rowspan cell from above
for row in table.find_all('tr')[1:]:
    covered = [col for col, left in spans.items() if left > 0]
    for col in covered:
        spans[col] -= 1
    free = [col for col in range(8) if col not in covered]
    cells = dict(zip(free, row.find_all(['th', 'td'], recursive=False)))
    for col, cell in cells.items():
        spans[col] = int(cell.get('rowspan', 1)) - 1

    if 0 in cells:  # a numbered row starts a new president
        name, lifespan = re.match(r'(.*?)\s*\((.*?)\)', clean(cells[2])).groups()
        presidents.append({
            'number': int(clean(cells[0])),
            'name': name,
            'lifespan': lifespan,
            'term': clean(cells[3]),
            'party': clean(cells[5]),
            'elections': [],
            'vice_presidents': [],
        })
    president = presidents[-1]
    if 6 in cells and clean(cells[6]):
        president['elections'].append(clean(cells[6]))
    if 7 in cells and clean(cells[7]):
        president['vice_presidents'].append(clean(cells[7]))

assert [p['number'] for p in presidents] == list(range(1, len(presidents) + 1))
with open('presidents_data.json', 'w') as f:
    json.dump(presidents, f, indent=2, ensure_ascii=False)
print("Presidents data has been saved to presidents_data.json")
