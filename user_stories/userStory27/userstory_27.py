#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import parser
import math
    
def individual_ages(individuals_dataframe):
    for i in range(len(individuals_dataframe)):
        name=individuals_dataframe[i]["name"]
        age=individuals_dataframe[i]["age"]
        message= "Name:" + name.replace("/"," ")+ "--->" + "Age:" +str(age)
        #print(message)
    return message

