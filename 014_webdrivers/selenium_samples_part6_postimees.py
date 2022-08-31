from selenium import webdriver
import datetime

url = 'https://rus.postimees.ee/'

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

agree_btn = driver.find_element('xpath', '/html/body/div[13]/div[2]/div/div[2]/div[2]')
agree_btn.click()

articles = driver.find_elements('class name', 'list-article')

article_list = []
for article in articles:
    link = article.find_element('tag name', 'a').get_attribute('href')

    heading = article.find_element('class name', 'list-article__headline').text
    article_item = {
        'heading': heading,
        'link': link
    }
    article_list.append(article_item)

print(article_list)
print(len(article_list))
driver.quit()

