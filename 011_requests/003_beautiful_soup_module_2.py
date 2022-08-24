from bs4 import BeautifulSoup as BS
import requests
import re

url = "https://gammatest.net/course/python/"
full_page = requests.get(url)

soup = BS(full_page.content, 'html.parser')

# # BS has children, html tag is a child of BS object
# print(len(soup.contents))
# print(soup.contents[2])
# print(soup.contents)


# # Reg Exp can be used too
# print(soup.find(re.compile('^me')))

# # Find many
# print(soup.find_all(['a', 'table']))

# # Find all existing tags
# for tag in soup.find_all(True):
#     print(tag.name)

# # Find by class name (using re)
# print(soup.find_all(class_=re.compile('md')))

# # Getting all string from html
# print(soup.find_all(string=True))

