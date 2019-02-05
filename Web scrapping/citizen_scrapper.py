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


driver = webdriver.Chrome(executable_path='C:/Users/kiran/Documents/chromedriver.exe')
driver.get('https://jobs.citizensbank.com/search-jobs')
time.sleep(10)
html = driver.page_source
soup = BeautifulSoup(html,"lxml")
a_href = soup.findAll('a', href=True)
ahref_soup = BeautifulSoup(str(a_href))
list_jobs = soup.findAll('section', id="search-results-list")
list_jobs_bs = BeautifulSoup(str(list_jobs))
text_append = 'https://jobs.citizensbank.com'
for div in list_jobs_bs.findAll('a'):
    if div.get('class') is None:
        url = div.get('href');
        final_url = text_append+url;
        print(final_url);


# In[15]:


click_next = driver.find_element_by_xpath('//*[@id="pagination-bottom"]/div[2]/a[2]')


# In[16]:


click_next.click()


# In[3]:


number_of_pages = soup.findAll("span",{"class","pagination-total-pages"})[0].string


# In[4]:


number_of_pages = re.sub("[^0-9]","",str(number_of_pages))
number_of_pages = int(number_of_pages)


# In[5]:


for page in range(1,int(number_of_pages)):
    click_next = driver.find_element_by_xpath('//*[@id="pagination-bottom"]/div[2]/a[2]')
    click_next.click()
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html,"lxml")
    a_href = soup.findAll('a', href=True)
    ahref_soup = BeautifulSoup(str(a_href))
    list_jobs = soup.findAll('section', id="search-results-list")
    list_jobs_bs = BeautifulSoup(str(list_jobs))
    text_append = 'https://jobs.citizensbank.com'
    for div in list_jobs_bs.findAll('a'):
        if div.get('class') is None:
            url = div.get('href')
            final_url = text_append+url
            print(final_url)


# In[ ]:




