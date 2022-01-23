import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

url ="http://naver.com"
browser.get(url)

# elem = browser.find_element_by_id("query")
# elem.send_keys("뉴스")
# elem.send_keys(Keys.ENTER)
elem = browser.find_element_by_class_name("link_news")
elem.click()

import time
interval = 2
time.sleep(interval)

url = browser.current_url
print(url)