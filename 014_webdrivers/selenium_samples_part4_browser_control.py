from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = 'https://www.youtube.com/user/NatureVideoChannel/videos?view=0&sort=p&flow=grid'

driver = webdriver.Chrome()
# Getting window width and height
width = driver.get_window_size().get('width')
height = driver.get_window_size().get('height')

# Set window size
driver.set_window_size(800, 600)

# Get window position
pos_x = driver.get_window_position().get('x')
pos_y = driver.get_window_position().get('y')
print(pos_x, pos_y)

# Set window position
driver.set_window_position(100, 100)

# Minimize, maximize, fullscreen
driver.fullscreen_window()
time.sleep(4)
driver.minimize_window()
time.sleep(4)
driver.maximize_window()

driver.get(url)

agree_btn = driver.find_element('xpath', '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button')
agree_btn.click()

# in order to save screenshot use .save_screenshot('filename')
driver.save_screenshot('images/main.png')

# in order to save element screenshot
banner = driver.find_element('xpath', '//*[@id="dismissible"]')
banner.screenshot('images/banner.png')

# get current url
print(driver.current_url)

# refresh page
driver.refresh()

# window handle (a unique code for opened window/tab, different for different sessions)
print(driver.current_window_handle)
original_window = driver.current_window_handle

# return all opened window handles
print(driver.window_handles)
# Create new window
driver.switch_to.new_window('tab')
# driver.switch_to.new_window('window')

# Switching between windows
driver.get('http://www.github.com')
second_tab = driver.current_window_handle
driver.switch_to.window(original_window)
driver.find_element('xpath', '//*[@id="video-title"]').send_keys(Keys.CONTROL + Keys.RETURN)
third_tab = driver.current_window_handle
driver.switch_to.window(original_window)

cnt = 0
for window in driver.window_handles:
    driver.switch_to.window(window)
    driver.save_screenshot(f'images/{cnt}.png')
    cnt += 1



