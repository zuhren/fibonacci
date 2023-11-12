#!/usr/bin/env python
# coding: utf-8

# In[111]:


import random

def enter_list(lst):
    while lst:
        chosen = random.sample(lst,2)
        print(chosen)
    
        for item in chosen:
            lst.remove(item)
        if len(lst) % 2 == 1:
            lst.append("   ")


# In[97]:


lst = ["sam", "dean", "jo", "sarah", "jones", "matthew", "samuel", "ted", "barney", "robin", "marshall", "lily", "joanna"]

enter_list(lst)


# In[110]:


random_list = ["metehan yalçın", "ibrahim tunç", "ali mirza", "buğra vural", "emre göktürkün gürel", "mukadder çelik", "neslihan köse", "özge özaydın", "berke", "bünyamin ince", "emirhan hamitoğlu"]

enter_list(random_list)

