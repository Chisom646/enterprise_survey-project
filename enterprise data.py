#!/usr/bin/env python
# coding: utf-8

# In[7]:


#import the data
import pandas as pd
enterprise_survey = pd.read_csv('Downloads\\enterprise_survey2023.csv')
enterprise_survey.head() #to bring out the top five rows in the database


# In[12]:


#Clean the data
enterprise_survey.duplicated() #to check for duplicates
enterprise_survey = enterprise_survey.drop_duplicates() #to remove the duplicates in the data set


# In[13]:


#check for null values and remove null values
enterprise_survey = enterprise_survey.dropna()




# In[18]:


#Perform dbms operations on the data base
# Adding a new record to the data
new_record = {
    'Year' : 2012,
    'Industry_aggregation_NZSIOC' : 'Level 3',
    'Industry_code_NZSIOC' : 'AA12',
    'Industry_name_NZSIOC' : 'Food Product manufacturing',
    'Units' : 'Percentage',
    'Variable_code' : 'H42',
    'Variable_name' : 'Total EXpenditure',
    'Variable_category' : 'Financial ratios', 
    'Value' :  57,
    'Industry_code_ANZSIC06' : 'ANZSIC06 divisions A-S (excluding classes K633..)'
}
enterprise_survey = pd.concat([enterprise_survey, pd.DataFrame([new_record])], ignore_index= True)
enterprise_survey.tail() #to check if the new record has been added


# In[22]:


# changing 'H' variable_code to 'A'
enterprise_survey["Variable_category"] = enterprise_survey["Variable_category"].replace("Financial ratios", "Finance Fraction")
enterprise_survey["Variable_category"]


# In[28]:


# to print all books where Units is Percentage
Percentage_Units = enterprise_survey[enterprise_survey['Units'].str.contains('Percentage', na = False , case =False)]
Percentage_Units


# In[33]:


#Filter for year 2023 only
filtering_year = enterprise_survey.query('2020 <= Year <= 2023')
filtering_year


# In[ ]:




