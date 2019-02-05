#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import sys
import time


# In[2]:
#if it does not work please check the path in the folder
executable_path='chromedriver.exe'
driver = webdriver.Chrome(executable_path)
driver.get('https://regions.wd5.myworkdayjobs.com/Regions_Careers')
time.sleep(10)
pause=2
lastHeight = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(pause)
    newHeight = driver.execute_script("return document.body.scrollHeight")
    if newHeight == lastHeight:
        break
    lastHeight = newHeight
html = driver.page_source
soup = BeautifulSoup(html,"lxml")
li_class = soup.findAll("li", { "class" : "WIYF WK3N WE5 WP-F" })
base_url = "https://regions.wd5.myworkdayjobs.com/en-US/Regions_Careers/job/"
for s in li_class:
    a = s.findAll("div",{"class","gwt-Label WOTO WISO"})[0].string
    c = re.sub("[^a-zA-Z]","-",str(a))
    b = s.findAll("span",{"class","gwt-InlineLabel WM-F WLYF"})[0].string
    try:
        d= b.split(" | ")[0]
        d= re.sub("[^a-zA-Z0-9]","",str(d))
        e= b.split(" | ")[1]
        e= re.sub("[^a-zA-Z0-9]","",str(e))
    except:
        d='null'
        e='null'
    final_url = base_url+d+"/"+c+"_"+e
    print(final_url)


# In[5]:





# In[ ]:





# In[ ]:





# In[ ]:




