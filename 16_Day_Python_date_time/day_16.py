# Exercises: Day 16
from datetime import datetime

now = datetime.now()

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()
print(day, month, year, hour, minute, timestamp)


t = now.strftime("%m/%d/%Y, %H:%M:%S")
print(t)


t1 = now.strftime("%d %B, %Y")
print(t1)

new_year = datetime(now.year + 1, 1, 1)
print('Time left until new year:', new_year - now)

epoch = datetime(1970, 1, 1)
print('Time since 1 January 1970:', now - epoch)

# What can the datetime module be used for?
# - Time series analysis (stock prices, sensor readings, weather data)
# - Timestamping activities in an application (logs, logins, audit trails)
# - Adding posts on a blog (published/updated dates)
# - Scheduling and reminders (deadlines, countdowns like the new year one above)
# - Calculating ages, durations, and subscription/expiry dates
