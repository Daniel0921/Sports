#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 


# In[3]:


pwd


# In[4]:


baseball1 = pd.read_csv("C:\\Users\\Danny\\Desktop\\baseball1.csv")
baseball1.head()


# In[5]:


baseball2 = pd.read_csv("C:\\Users\\Danny\\Desktop\\baseball2.csv")
baseball2.head()


# In[6]:


merge = pd.merge(baseball1, baseball2, on = ['First'], how = 'left')
merge.head(55)


# In[7]:


merge2 = pd.merge(baseball1, baseball2, on = ['First', 'Last'], how = 'left')
merge2.head(50)


# In[8]:


merge2[merge2.R>80].reset_index(drop = True)


# In[9]:


merge2_new = merge2.rename(columns={"2B":"Double"})
merge2_new[(merge2_new.Double>30)&(merge2_new.LEAGUE == 'AL')].reset_index(drop = True)


# In[10]:


merge2_reborn = merge2.rename(columns={"2B":"Double", "3B":"Triple"})
merge2_reborn[(merge2_reborn.Triple > 5) | (merge2_reborn.HR > 30)].reset_index(drop = True)


# In[11]:


Avg = merge2['H']/merge2['AB']
merge2['Avg'] = Avg.round(3)
merge2.head(15)


# In[73]:


merge2_infinity = merge2.sort_values('Avg', ascending = False).reset_index(drop = True)
merge2_infinity.head(10)


# In[12]:


merge2_select = merge2[['First', 'Last', 'R', '3B', 'RBI']]
merge2_select.head(15)

