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
Mr. Jones
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
abc

ball mall hall wall tall
'''
sentence = 'Start a sentence and then bring it to an end'


# Other methods #


# # Finds all matches and creates an iterable object
# pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
# matches = pattern.finditer(text_to_search)


# # Findall will search for all matches of groups if there is any or whole expression
# pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')  # One group example
# # pattern = re.compile(r'\d{3}.\d{3}.\d{4}')  # No group example
#
# matches = pattern.findall(text_to_search)

# # Match method only sees if beginning of string is matching
# pattern = re.compile(r'Start')
# # pattern = re.compile(r'sentence')  # Will return None
#
# matches = pattern.match(sentence)  # Match doesn't return iterable, returns first match or None

# # Search is similar to match, but will look everywhere
# pattern = re.compile(r'bring')
#
# matches = pattern.search(sentence)  # Search doesn't return iterable, returns first match or None


# Flags #
# Check re_flags.png for reference
# pattern = re.compile(r'start')
# pattern = re.compile(r'start', re.IGNORECASE)  # re.IGNORECASE ignores casesensitive letters
# pattern = re.compile(r'start', re.I)  # Is same as re.IGNORECASE

matches = pattern.search(sentence)




# # For loop to print out matches
# for match in matches:
#     print(match)

print(matches)