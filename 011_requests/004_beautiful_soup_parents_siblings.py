from bs4 import BeautifulSoup as BS
import requests
import re

url = "https://gammatest.net/course/python/"
full_page = requests.get(url)

soup = BS(full_page.content, 'html.parser')

# # find_all(True) will return all available tags
# for tag in soup.find_all(True):
#     print(tag.name)

# # Find by link text
# print(soup.find_all(href=re.compile("git-scm.com")))

# # Find all links by text
# print(soup.find_all('a', text="Перейти"))
# print(soup.find_all(text='Перейти'))

# # Find links by string
# print(soup.find_all('a', string="Eesti keeles"))
# print(soup.find_all(string="Eesti keeles"))

# # Limit argument
# print(soup.find_all('a', text="Перейти", limit=2))

# # Calling a tag is same as find_all
# print(soup.find_all('title'))
# print(soup('title'))

# # Find parent/parents
# test_link = soup.find('a', string='Eesti keeles')
# print(test_link.find_parents('div'))
# print(test_link.find_parent('div'))

# Find siblings
first_link = soup.find('td')
# print(first_link.find_next_siblings('td'))
# print(first_link.find_next_sibling('td'))
# # Find all next will return all next tags (siblings)
# print(first_link.find_all_next('td'))
# # Find next will return one only
# print(first_link.find_next('td'))

