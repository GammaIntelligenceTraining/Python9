string_sample = "Hello world world"
string_sample2 = "first letteR is lowErcase"
string_sample3 = " extra whitespace string "
german_sample = "der Fluß"


print(string_sample[1])  # Will return second letter from a string
print(string_sample[4:])  # Will return all letters from fifth
print(string_sample[:14])  # Will return all letters from begining to the 14th
print(string_sample[5:12])  # Will return part of a string indexed in []
print(string_sample[1:10:2])  # Will print every second value from range
print(string_sample[::-1])  # will print string backwards

print(len(string_sample))  # Will return length of string

print("world" in string_sample)  # Will return True if given argument is part of the string, or False if not. (not in is opposite)

print(string_sample.upper())  # Will convert string to uppercase

print(string_sample.lower())  # Will convert string to lowercase

print(german_sample.lower())
print(german_sample.casefold())  # Will return lowercase string

print(string_sample2.capitalize())  # Will return string with first letter in uppercase

print(string_sample3.strip())  # Will remove extra whitespaces (begining and end of string)

print(string_sample.replace('world', 'people'))  # Will replace one part of the string with other

print(string_sample.split(' '))  # Converts to list with specified delimiter

print(string_sample.count('o'))  # Will return number of times specified value occurs in string as (INT)

print(string_sample.find('world'))  # Will return index of specified value (first time occurs)

# Will print each letter in a new row (string is iterable object)
# for letter in string_sample:
# 	print(letter)
