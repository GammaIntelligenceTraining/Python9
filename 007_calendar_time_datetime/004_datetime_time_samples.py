import datetime

t = datetime.time(13, 24, 10)
print(t)  # Will print time with all parameters
print(t.hour)  # Will print only hours

dt = datetime.datetime(2020, 11, 30, 18, 20, 36, 100000)
print(dt)
print(dt.date())  # Will print date only
print(dt.time())  # Will print time only

dt_delta = datetime.timedelta(days=7, hours=15, minutes=10)
print(dt + dt_delta)  # Will print datetime after timedelta

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
print(dt_today)
print(dt_now)

print(dt_today.strftime('%B %d, %Y'))  # Will print formated date where %B is full month, %d day as number, %Y full year in YYYY format

dt_str = 'November 30, 2020'
dt_str = 'Nov 30, 2020'
print(dt_str)
str_to_date = datetime.datetime.strptime(dt_str, '%b %d, %Y')  # Converts string into datetime format
print(str_to_date)
print(type(str_to_date))

dt_str3 = '7 Июнь 2021, 12:56'
dt_str3 = dt_str3.replace('Июнь', 'June')
str_to_date3 = datetime.datetime.strptime(dt_str3, '%d %B %Y, %H:%M')
print(str_to_date3)
print(type(str_to_date3))