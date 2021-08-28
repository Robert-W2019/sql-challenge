#!/usr/bin/env python
# coding: utf-8

# # Dependencies

# In[2]:


get_ipython().system('pip install psycopg2')


# In[36]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from config import username, password
get_ipython().run_line_magic('matplotlib', 'inline')

from sqlalchemy import create_engine
engine = create_engine(f'postgresql://{username}:{password}@localhost:5432/employee_db_challenge')
connection = engine.connect()



# # Import the Employees Table

# In[5]:


employees = pd.read_sql('select * from employees', connection, parse_dates = ['birth_date', 'hire_date' ])
employees.head()


# # Import the Departments Table

# In[6]:


departments = pd.read_sql('select * from departments', connection)
departments.head()


# # Import the Salaries Table

# In[28]:


salaries = pd.read_sql('select * from salaries', connection)
salaries


# # Import the Department Manager Table

# In[8]:


dept_manager = pd.read_sql('select * from dept_manager', connection)
dept_manager.head()


# # Import the Titles Table

# In[13]:


titles = pd.read_sql('select * from titles', connection)
titles


# # Import the Department Employee Table

# In[11]:


dept_emp = pd.read_sql('select * from dept_emp', connection)
dept_emp.head()


# # Data Analysis

# In[12]:


titles.title.value_counts()


# In[43]:


#Create a histogram to visualize the most common salary ranges for employees.
#referenced https://pythonspot.com/matplotlib-histogram/
salaries_extract = salaries['salary']

bins = 4
n, bins, patches = plt.hist(salaries_extract, bins, facecolor='green', alpha=0.5)

plt.xlabel('Salary Amount')
plt.ylabel('Number of Employees')
plt.title('Five Most Common Salary Ranges For Employees')
plt.show()


# In[ ]:





# In[ ]:




