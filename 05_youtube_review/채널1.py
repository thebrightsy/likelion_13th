import pandas as pd
from selenium import webdriver
import time
url="https://www.youtube.com/watch?v=umpsXnXNkos"
# page=urlopen(url)
# soup=BeautifulSoup(page, 'html.parser')
# print(soup.title)

driver = webdriver.Chrome("chromedriver_93")
driver.get(url)
time.sleep(7)
# xpath 획득
# 획득된 sel.text로 확인
# //*[@id="count"]/ytd-video-view-count-renderer/span[1]
sel_search = driver.find_element_by_xpath('//*[@id="count"]/ytd-video-view-count-renderer/span[1]')

print(sel_search.tag_name)
print(sel_search.text)

