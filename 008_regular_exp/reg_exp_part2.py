import re

# Sample string
text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa HaHaH
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
example.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
900A555A1234
Mr. Jones
Mr Smith
Ms Davis
Mrs. Robinson
Mr. JoNeS
Mr. T
Ms. Davis9876
Mrs Robinson_
abc

ball mall hall wall tall
'''

sentence = 'Start a sentence and then bring it to an end'

# Selectors and anchors #

# Selector
pattern = re.compile(r'\s')

# Anchor
pattern = re.compile(r'\BHa')
# pattern = re.compile(r'^Start')
# pattern = re.compile(r'end$')

# matches = pattern.finditer(sentence)
# matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match)


# Creating patterns #
# Check cheat_sheet.txt for keys

# Matching phone numbers
# pattern = re.compile(r'\d\d\d')  # Will select 3 digits matches
# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')


# # Matching phone numbers
# # Character set is created by putting characters into []
# # pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')  # Will match only one character at a time
# pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')  # Will match only one character at a time


# Selecting range of characters
# pattern = re.compile(r'[1-5]')  # Matches all numbers from 1 to 5 (only one digit)
# pattern = re.compile(r'[a-z]')  # Matches all letters from a to z (only one letter)

# pattern = re.compile(r'[a-zA-Z]')  # Matches all letters from aA to zZ (only one letter)
# pattern = re.compile(r'[^a-zA-Z]')  # ^ carrot sign inside []
# pattern = re.compile(r'[^w]all')  # Matches all but starting with w


# # Quantifiers
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')  # Number between {} tells how many matches to search

# # Matching names
# pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z][a-zA-Z]*')
# # pattern = re.compile(r'Mr\.?\s[A-Z]\w*')  # Will select all misters
# # pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')  # Will select all ms mr mrs

# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(match)

# Working with file
with open('people.txt', 'r', encoding='UTF8') as file:
    people_data = file.read()

    # Match all phones from file
    pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
    matches = pattern.finditer(people_data)

    for match in matches:
        print(match)
