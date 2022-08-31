from selenium import webdriver

url = 'https://www.youtube.com/user/NatureVideoChannel/videos?view=0&sort=p&flow=grid'

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

agree_btn = driver.find_element('xpath', '/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[2]/div/div/button')
agree_btn.click()

videos = driver.find_elements('class name', 'style-scope ytd-grid-video-renderer')

video_list = []
for video in videos:
    # '.' in front of xpath will search inside element not page
    title = video.find_element('xpath', './/*[@id="video-title"]').text
    views = video.find_element('xpath', './/*[@id="metadata-line"]/span[1]').text
    added = video.find_element('xpath', './/*[@id="metadata-line"]/span[2]').text
    link = video.find_element('xpath', './/*[@id="video-title"]').get_attribute('href')
    # print(title, views, added)

    vid_item = {
        'title': title,
        'views': views,
        'added': added,
        'link': link
    }
    video_list.append(vid_item)

print(video_list)
print(len(video_list))