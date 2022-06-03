#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
from datetime import date, datetime
import csv
import requests
import json
import re


# In[2]:


results = []

with open("shopee_shoe_size.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader)
    
    for row in csv_reader:
        template = "https://shopee.co.id/api/v4/item/get?itemid={}&shopid={}"
        page_request = requests.get(template.format(row[1], row[0]))
        soup = BeautifulSoup(page_request.content, 'html5lib')
        
        json_data = json.loads(soup.text)
        plist = json_data['data']['models']
        
        for i in range(len(plist)):
            temp = []
            temp.append(datetime.now())
            temp.append(row[0])
            temp.append(plist[i].get("itemid"))
            temp.append(re.findall(r'[A-Za-z]+|\d+', plist[i].get("name")))
            temp.append(plist[i].get("stock"))
            
            results.append(temp)


# In[3]:


filename = "{}_shoe_size_data.csv".format(date.today())
with open(filename, 'w') as f:
    writer = csv.writer(f)
    writer.writerows(results)


# In[ ]:




