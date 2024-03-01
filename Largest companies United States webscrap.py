#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime
import smtplib
import pandas as pd 


# In[2]:


URL = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(URL)
soup1= BeautifulSoup(page.content, "html")
print(soup1)


# In[39]:


table = soup1.find_all('table')[1]
print(table)


# In[40]:


soup1.find('table', class_ = "wikitable sortable")


# In[49]:


world_titles = table.find_all('th')


# In[ ]:





# In[50]:


world_table_title = [title.text.strip() for title in world_titles]

print(world_table_title)


# In[52]:


df = pd.DataFrame(columns = world_table_title)
df


# In[61]:


column_data = table.find_all('tr')


# In[65]:


for row in column_data[1:]: 
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    lenght = len(df)
   
    df.loc[lenght] = individual_row_data
    #print(individual_row_data)


# In[66]:


df


# In[68]:


df.to_csv(r'C:\Users\juani\OneDrive\Desktop\PYTHON\myexercises\webscrap\ranking_usa_companies.csv', index=False)


# In[ ]:




