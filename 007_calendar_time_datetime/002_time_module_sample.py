import time
# Documentation for time module
# https://docs.python.org/3/library/time.html


start = time.time()
time.sleep(7)  # Will pause program for seconds given in ()

print(time.time())  # Will return time as a UNIX timestamp (time from 1 Jan 1970 00:00:00)

print(time.asctime())  # Will return time now

print(time.gmtime())  # struct_time format
print(type(time.gmtime()))

now = time.gmtime()
print(now[0])  # Will print tm_year

print(now[3])  # Will print tm_hour

now2 = time.asctime()  # Prints time in more suitable format
print(now2)

stop = time.time()
print(stop - start)  # Will count difference between start and stop variables