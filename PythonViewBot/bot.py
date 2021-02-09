#Selenium Webdriver must be installed for this to work

import time;
from selenium import webdriver;

#time to refresh page (seconds)
Timer = 10

#youtube link
link = 'https://m.youtube.com/watch?v=fJN2MqzkX2c'

#number of views
views = 9999

driver = webdriver.Chrome()
driver.get(link)

for i in range(views):
    time.sleep(Timer)
    driver.refresh()
  
