#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


data = pd.read_excel(r"C:\Users\MANTHAN SHARMA\Downloads\Customer Call List.xlsx")
pd.set_option('display.max.rows', 25)
data


# In[4]:


data = data.drop_duplicates()
data


# In[5]:


data= data.drop(columns = 'Not_Useful_Column')
data


# In[6]:


# data['Last_Name']=data['Last_Name'].str.lstrip('/')
# data['Last_Name']=data['Last_Name'].str.lstrip('..')
# data['Last_Name']=data['Last_Name'].str.rstrip('_')
data['Last_Name']=data['Last_Name'].str.strip('123._/')
data


# In[7]:


data["Phone_Number"]=data["Phone_Number"].str.replace('[^a-zA-Z0-9]','', regex = True)
data


# In[8]:


data['Phone_Number'] = data['Phone_Number'].apply(lambda x : str(x))


# In[9]:


data['Phone_Number'] = data['Phone_Number'].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])
data


# In[10]:


data['Phone_Number'] = data['Phone_Number'].str.replace("nan--",'')


# In[11]:


data['Phone_Number'] = data['Phone_Number'].str.replace("Na--",'')
data


# In[12]:


data[['Street_Address', 'State', 'Zip_code']] = data['Address'].str.split(',',n=2,expand = True)


# In[13]:


data.drop(columns = 'Address', inplace = True)
data


# In[14]:


data['Do_Not_Contact'] = data['Do_Not_Contact'].fillna('')
data


# In[15]:


data['Paying Customer']=data['Paying Customer'].str.replace('Yes','Y')
data['Paying Customer']=data['Paying Customer'].str.replace('No','N')
data


# In[16]:


data['Do_Not_Contact']=data['Do_Not_Contact'].str.replace('Yes','Y')
data['Do_Not_Contact']=data['Do_Not_Contact'].str.replace('No','N')
data


# In[17]:


data = data.fillna("")
data


# In[18]:


for x in data.index:
    if data.loc[x, 'Phone_Number'] == '' or data.loc[x, 'Do_Not_Contact']=='Y' :
        data.drop(x, inplace = True)

data


# In[19]:


data.reset_index(drop = True, inplace = True)
data


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




