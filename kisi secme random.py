#!/usr/bin/env python
# coding: utf-8

# In[67]:


import random


lst = ["sam", "dean", "jo", "sarah", "jones", "matthew", "samuel", "ted", "barney", "robin", "marshall", "lily", "joanna", "noah"]
while lst:
    chosen = random.sample(lst,2)
    print(chosen)
    
    for item in chosen:
        lst.remove(item)
    

