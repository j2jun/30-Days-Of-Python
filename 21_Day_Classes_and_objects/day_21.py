# Exercises: Level 1
from collections import Counter


class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return round(self.sum() / self.count())

    def median(self):
        s = sorted(self.data)
        mid = len(s) // 2
        return s[mid] if len(s) % 2 else (s[mid - 1] + s[mid]) / 2

    def mode(self):
        value, count = Counter(self.data).most_common(1)[0]
        return {'mode': value, 'count': count}

    def var(self):
        m = self.sum() / self.count()
        return round(sum((x - m) ** 2 for x in self.data) / self.count(), 1)

    def std(self):
        return round(self.var() ** 0.5, 1)

    def freq_dist(self):
        return sorted(((c / self.count() * 100, x) for x, c in Counter(self.data).items()), reverse=True)

    def describe(self):
        mode = self.mode()
        return '\n'.join([
            f'Count: {self.count()}',
            f'Sum:  {self.sum()}',
            f'Min:  {self.min()}',
            f'Max:  {self.max()}',
            f'Range:  {self.range()}',
            f'Mean:  {self.mean()}',
            f'Median:  {self.median()}',
            f"Mode:  ({mode['mode']}, {mode['count']})",
            f'Variance:  {self.var()}',
            f'Standard Deviation:  {self.std()}',
            f'Frequency Distribution: {self.freq_dist()}',
        ])


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)

print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
print()
print(data.describe())

#Exercises: Level 2
class PersonAccount:
    def __init__(self, firstname, lastname, incomes=None, expenses=None):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes or []    # list of (amount, description)
        self.expenses = expenses or []  # list of (amount, description)

    def total_income(self):
        return sum(amount for amount, _ in self.incomes)

    def total_expense(self):
        return sum(amount for amount, _ in self.expenses)

    def add_income(self, amount, description):
        self.incomes.append((amount, description))

    def add_expense(self, amount, description):
        self.expenses.append((amount, description))

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        return (f'{self.firstname} {self.lastname} | income: {self.total_income()}, '
                f'expense: {self.total_expense()}, balance: {self.account_balance()}')

    def __str__(self):
        return self.account_info()


account = PersonAccount('Asabeneh', 'Yetayeh', [(5000, 'salary')], [(1200, 'rent')])
account.add_income(800, 'freelance')
account.add_expense(300, 'groceries')
print()
print(account.incomes)   # [(5000, 'salary'), (800, 'freelance')]
print(account.expenses)  # [(1200, 'rent'), (300, 'groceries')]
print(account)           # Asabeneh Yetayeh | income: 5800, expense: 1500, balance: 4300
