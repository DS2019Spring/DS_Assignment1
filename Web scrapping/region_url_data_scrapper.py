#!/usr/bin/env python
# coding: utf-8

# In[7]:


from urllib.parse import urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup
from IPython.core.display import display, HTML
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import re
import sys
import time


# In[119]:


url='https://regions.wd5.myworkdayjobs.com/en-US/Regions_Careers/job/Fairhope/Mortgage-Loan-Originator--Greater-Fair-Hope-Area--AL_R23593'


# In[120]:


driver = webdriver.Chrome(executable_path='C:/Users/kiran/Documents/chromedriver.exe')
driver.get(url)
time.sleep(5)
html = driver.page_source
soup=BeautifulSoup(html)


# In[121]:


body = soup.findAll("div",{"class","GWTCKEditor-Disabled"})[1]


# In[122]:


body


# In[71]:


body = BeautifulSoup(str(body))


# 

# In[110]:


for text in body.findAll("span"):
    text1 = BeautifulSoup(str(text))
    text2 = text1.find('span').get_text()
    print(text2)


# In[115]:


body1 = str(body).replace("<span><span>","")


# In[124]:


body2 = str(body1).replace("</span></span>","")


# In[125]:


for text in BeautifulSoup(body2).findAll("span"):
    text1 = BeautifulSoup(str(text))
    text2 = text1.find('span').get_text()
    print(text2)


# In[ ]:




