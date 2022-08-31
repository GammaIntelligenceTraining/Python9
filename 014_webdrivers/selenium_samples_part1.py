from selenium import webdriver
# Will import methods that allow usage of keys like Enter, Esc etc.
from selenium.webdriver.common.keys import Keys
import time

# Specify browser driver location
driver_location = "chromedriver.exe"

# Connect browser driver
driver = webdriver.Chrome(driver_location)

# get() command will open browser and visit page given in ()
driver.get('https://github.com/')

# close() command will close tab
# driver.close()

# # quit() command will close browser
# driver.quit()

print(driver.title)
search = driver.find_element('name', 'user_email')

# search.is_displayed() - Whether the element is visible to a user.
# search.is_selected() - Returns whether the element is selected.
# search.is_enabled() - Returns whether the element is enabled.
if search.is_enabled() == True:
    print('All is good')
    search.send_keys('python@mrartful.com')
    search.send_keys(Keys.RETURN)
else:
    print('Program crashed')

time.sleep(10)
continue_button = driver.find_element('class name', 'signup-continue-button')
continue_button.click()

password_field = driver.find_element('id', 'password')
password_field.send_keys('12345678asd')

time.sleep(10)
continue_button = driver.find_element('xpath', '//*[@id="password-container"]/div[2]/button')
continue_button.click()
login = driver.find_element('id', 'login')
login.clear()
login.send_keys('mrArtful')


# # Returns source code of opened webpage
# print(driver.page_source)
