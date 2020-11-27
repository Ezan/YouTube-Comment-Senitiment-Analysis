#!/usr/bin/env python
# coding: utf-8

# In[6]:


from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

import sys



browser = webdriver.Chrome(executable_path='chromedriver.exe')

# load the first page
browser.get('https://www.youtube.com/results?search_query={}'.format(sys.argv[-1]))

#browser.get('https://www.youtube.com/results?search_query=postmalone-sunflower')

# Wait 15 seconds for page to load, if page doesn't load, we are throwing exception
timeout = 15
try:
   WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="img"]')))
except TimeoutException:
   print('sorry.. no opening')
   browser.close()

print('downloading page')
time.sleep(5)
browser.find_element_by_xpath('//*[@id="video-title"]').click()

time.sleep(5)
print('now scrolling')
stop_error = False
scroll_Down = 5000
count = 0

while True:
    count += 1
    browser.execute_script("window.scrollTo(0, {})".format(scroll_Down))
    time.sleep(3)
    browser.execute_script("window.scrollTo({}, {})".format(scroll_Down,scroll_Down-2000))
    scroll_Down+= 3000
    time.sleep(5)
    print('scrolling down')
    if count > 10 :
        print("finished scrolling")
        break


#browser.close()
comments = browser.find_elements_by_xpath('//*[@id="content-text"]')
comments = [i.text.replace(",","").replace("\n", " ") for i in comments if len(i.text) < 100]
a=0
with open('scrape.csv', 'w', encoding='utf-8') as f:
    f.write("id,"+'comment_text'+'\n')
    for text in comments :
        f.write(str(a)+","+text.lower() + '\n')
        a+=1







