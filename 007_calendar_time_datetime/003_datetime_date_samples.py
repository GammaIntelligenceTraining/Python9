import datetime

# Documentation for datetime module
# https://docs.python.org/3/library/datetime.html

# Single dates
d = datetime.date(2018, 7, 22)  # Need arguments not to get an error, 07 will give error too
print(d)
print(type(d))

today = datetime.date.today()  # Will return date today (according to system date and time)
print(today)

print(today - d)

print(today.year)  # Will return only year
print(today.day)  # Will return only day
print(today.month)

print(today.weekday())  # Monday 0 Sunday 6
print(today.isoweekday())  # Monday 1 Sunday 7

# Time deltas
tdelta = datetime.timedelta(days=7)  # Will return time delta equal to 7 days
print(today + tdelta)  # Will print date 7 days from today

# Adding timedelta to date will return date data type, substracting date from a date will return timedelta data type
# date2 = date1 + timedelta
# timedelta = date1 - date2

bday = datetime.date(2021, 3, 16)
till_bday = bday - today
print(till_bday)  # Will return days and hours until bday
print(till_bday.days)  # Will return only days until bday
print(till_bday.total_seconds())  # Will return seconds until bday
