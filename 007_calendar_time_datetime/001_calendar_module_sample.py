import calendar
# Documentation for Calendar module
# https://docs.python.org/3/library/calendar.html


# W stands for width, L stands for length
print(calendar.month(2020, 11, w=10, l=0))

# Will print calendar for whole year C stands for distandce between two month and M for amount of month in on row
print(calendar.calendar(2020, w=2, l=1, c=2, m=3))

print(calendar.weekday(2020, 11, 30))  # Will print weekday number (MONDAY is 0 and SUNDAY is 6)

print(calendar.isleap(2020))  # Will return True because 2020 is a leap year
print(calendar.isleap(2018))  # Will return False because 2020 is not a leap year

print(calendar.leapdays(2000, 2020))  # Will return number of leap years between 2000 and 2020
