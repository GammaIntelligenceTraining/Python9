from bs4 import BeautifulSoup as BS
import requests

# First install required modules
# pip install bs4
# pip install requests

# Documentation
        # https://www.crummy.com/software/BeautifulSoup/bs4/doc/

url = "https://gammatest.net/course/python/"
full_page = requests.get(url)
# # .text will return prettified html string
# print(full_page.text)
# # .content will return html string
# print(full_page.content)

soup = BS(full_page.content, 'html.parser')
# # Returns html string
# print(soup)



# # Returns indented html string
# print(soup.prettify())

# # Get page title
# print(soup.title)

# # Or you can get page title value
# print(soup.title.text)

# # Get tag name
# print(soup.title.name)

# # Get name of a parent tag
# print(soup.title.parent.name)

# # Get all text from HTML
# print(soup.get_text)

# # Get class of a tag
# print(soup.div['class'])

# # Getting all divs on a page
# print(soup.div)

# # Getting div with specific class
# match = soup.find("div", class_='header')
# print(match)

# # Getting more specific
# match = soup.find("div", class_='col-md-4 col-sm-12')
# print(match.h2.text)

# # Getting all data
# for item in soup.find_all("div", class_='col-md-4 col-sm-12'):
#     print(item.h2.text)

# # Getting all data using findAll
# match = soup.findAll("div", class_="col-md-4 col-sm-12")
# print(type(match))
# print(len(match))
# print(match[0])

# for item in match:
#     print(item)

# # Returns list of attributes
# print(soup.div.get_attribute_list('class'))


