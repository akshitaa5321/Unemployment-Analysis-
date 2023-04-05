#!/usr/bin/env python
# coding: utf-8

# # UNEMPLOYMENT ANALYSIS

# In[24]:


#importing libraries
get_ipython().system('pip install plotly')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px  


# In[5]:


df1=pd.read_csv("Unemployment in India.csv") 
df1


# In[6]:


df2=pd.read_csv("Unemployment_Rate_upto_11_2020.csv") 
df2


# In[8]:


df=pd.read_csv("Unemployment in India.csv")
df=pd.read_csv("Unemployment_Rate_upto_11_2020.csv")
df                                            


# In[9]:


df.head(10)


# In[10]:


df.tail(10)


# In[11]:


df.info


# In[12]:


df.describe()


# In[13]:


df.columns


# In[14]:


df[' Frequency'].value_counts()


# In[15]:


print(df['Region.1'].value_counts())
print(df['Region'].value_counts())


# In[16]:


df.isnull().sum()


# In[17]:


df.duplicated().sum()


# In[18]:


print('Rows:',df.shape[0])
print('Columns:',df.shape[1])


# In[19]:


df.dtypes


# In[20]:


df[["day", "month", "year"]] = df[' Date'].str.split("-", expand = True)
df


# In[21]:


df.drop(columns=[' Frequency'],axis=1,inplace=True)


# In[22]:


df[:5]


# In[25]:


plt.figure(figsize=(5,5))
sns.heatmap(df.corr(),annot=True)
plt.show()


# In[26]:


plt.figure(figsize=(10,10))
plt.title("Unemployment in india")
sns.histplot(x=' Estimated Unemployment Rate (%)',hue= "Region", data=df,kde=False)
plt.show()


# In[27]:


sns.barplot(x='month',y=' Estimated Unemployment Rate (%)',hue='year',data=df)


# In[28]:


sns.barplot(x='day',y=' Estimated Unemployment Rate (%)',hue='year',data=df)


# In[29]:


sns.set_theme(style="ticks", palette="pastel")

# Draw a nested boxplot to show bills by day and time
sns.boxplot(x="month", y=' Estimated Employed', palette=["m", "g"],
            data=df)
sns.despine(offset=10, trim=True)


# In[30]:


df.drop('year',axis=1)


# In[31]:


plt.figure(figsize=(10,10))
plt.title("Unemployment in india")
sns.barplot(x='month',y =' Estimated Unemployment Rate (%)',hue='Region.1', data=df)
plt.show()


# In[32]:


plt.figure(figsize=(10,10))
plt.title("Unemployment in india")
sns.barplot(x='day',y =' Estimated Unemployment Rate (%)',hue='Region.1', data=df)
plt.show()


# In[33]:


unemploment = df[["Region",' Estimated Unemployment Rate (%)']]
figure = px.sunburst(unemploment, path=["Region"], 
                     values=' Estimated Unemployment Rate (%)',
                     width=700, height=700, color_continuous_scale="RdY1Gn", 
                     title="Unemployment Rate in India")
figure.show()   


# In[34]:


unemploment = df[["Region.1",' Estimated Employed']]
figure = px.sunburst(unemploment, path=["Region.1"], 
                     values=' Estimated Employed',
                     width=700, height=700, color_continuous_scale="RdY1Gn", 
                     title="employment Rate in India")
figure.show()

