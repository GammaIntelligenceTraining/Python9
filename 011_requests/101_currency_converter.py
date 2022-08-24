import requests
from bs4 import BeautifulSoup as BS

def user_choice():
    try:
        user_input = input("Please choose: \n"
                           "1. Convert RUB to EUR \n"
                           "2. Convert EUR to RUB \n"
                           "-->")
        if user_input == '1':
            ammount = float(input('Please enter ammount: '))
            result = ammount / get_eur_to_rub()
            print(result, 'Euro')
        elif user_input == '2':
            ammount = float(input('Please enter ammount: '))
            result = ammount * get_eur_to_rub()
            print(result, 'Russian Rubles')
    except:
        print('Error')
        user_choice()

def get_eur_to_rub():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
    eur_to_rub_url = 'https://www.google.com/search?sxsrf=ALeKk026VSJV_KaylKj6xYcHem-k7nvUuA%3A1608570709664&source=hp&ei=VdfgX6yWJuWjjgbAh6bgBA&q=eur+to+rub&oq=eur+to&gs_lcp=CgZwc3ktYWIQAxgAMgwIIxDJAxAnEEYQggIyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEMyBAgAEEM6BAgjECc6BwgAEMkDEEM6CAguEMcBEKMCOgIILjoCCAA6CQgjECcQRhCCAjoICAAQyQMQkQJQznFYyYgBYKidAWgAcAB4AIABnQGIAd0EkgEDNC4ymAEAoAEBqgEHZ3dzLXdpeg&sclient=psy-ab'
    full_page = requests.get(eur_to_rub_url, headers=headers)
    soup = BS(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    eur_to_rub_string = convert[0].text
    eur_to_rub_float = float(eur_to_rub_string.replace(',', '.'))
    return eur_to_rub_float

user_choice()