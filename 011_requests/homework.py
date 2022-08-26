import requests
from bs4 import BeautifulSoup as BS

url = 'https://www.ilmateenistus.ee/ilm/ilmavaatlused/vaatlusandmed/oopaevaandmed/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

r = requests.get(url, timeout=5, headers=headers)

soup = BS(r.content, 'html.parser')

table = soup.find('tbody').find_all('tr')

results = {}

for tr in table:
    results[tr.find_all('td')[0].text] = [tr.find_all('td')[1].text, tr.find_all('td')[2].text,
                                          tr.find_all('td')[3].text, tr.find_all('td')[4].text,
                                          tr.find_all('td')[5].text, tr.find_all('td')[6].text,
                                          tr.find_all('td')[7].text, tr.find_all('td')[8].text,
                                          tr.find_all('td')[9].text, tr.find_all('td')[10].text,
                                          tr.find_all('td')[11].text]



def main():
    user_choice = input('Please choose:\n'
                        '1. Õhutemperatuur\n'
                        '2. Maapinna temperatuur\n'
                        '3. Õhuniiskus\n'
                        '4. Tuule kiirus\n'
                        '5. Sademed\n'
                        '6. Päikesepaiste kestus\n'
                        '0. Exit\n'
                        '--> ')
    if user_choice == '1':
        for key in results:
            print()
            print(key)
            print(f'Keskmine {results[key][0]}')
            print(f'Max {results[key][1]}')
            print(f'Min {results[key][2]}')
        main()
    elif user_choice == '2':
        for key in results:
            print()
            print(key)
            if results[key][3] == '':
                print('Andmed puudu')
            else:
                print(f'Maapinna minimaalne temperatuur {results[key][3]}')
            if results[key][4] == '':
                print('Andmed puudu')
            else:
                print(f'Minimaalne 2cm kõrgusel {results[key][4]}')
        main()
    elif user_choice == '3':
        for key in results:
            print()
            print(key)
            print(f'Keskmine {results[key][5]}')
            print(f'Minimum {results[key][6]}')
        main()
    elif user_choice == '4':
        for key in results:
            print()
            print(key)
            if results[key][7] == '':
                print('Andmed puudu')
            else:
                print(f'Keskmine {results[key][7]}')
            if results[key][8] == '':
                print('Andmed puudu')
            else:
                print(f'Maksimum {results[key][8]}')
        main()
    elif user_choice == '5':
        for key in results:
            print()
            print(key)
            if results[key][9] == '':
                print('Andmed puudu')
            else:
                print(results[key][9])
        main()
    elif user_choice == '6':
        for key in results:
            print()
            print(key)
            if results[key][10] == '':
                print('Andmed puudu')
            else:
                print(results[key][10])
        main()
    elif user_choice == '0':
        exit()
    else:
        print('Choice is out of range')
        main()
main()