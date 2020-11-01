#!/usr/bin/env python
# coding: utf-8

# In[171]:


import numpy as np
import pandas as pd
import itertools 

d = pd.read_csv("data.csv")


# In[172]:


p = np.ones(300)
c1 = np.ones(300)
c2 = np.ones(300)
c3 = np.ones(300)
c4 = np.ones(300)
c5 = np.ones(300)


# In[173]:


for i in range(300):
    p[i] = d["p"][i]
    c1[i] = d["c1"][i]
    c2[i] = d["c2"][i]
    c3[i] = d["c3"][i]
    c4[i] = d["c4"][i]
    c5[i] = d["c5"][i]


# In[157]:


def jaccard(labels1, labels2):
    
    n11 = n10 = n01 = 0
    n = len(labels1)
    for i, j in itertools.combinations(range(n), 2):
        comembership1 = labels1[i] == labels1[j]
        comembership2 = labels2[i] == labels2[j]
        if comembership1 and comembership2:
            n11 += 1
        elif comembership1 and not comembership2:
            n10 += 1
        elif not comembership1 and comembership2:
            n01 += 1
    return float(n11) / (n11 + n10 + n01)


# In[180]:


jaccard(p, c1)


# In[176]:


jaccard(p, c2)


# In[177]:


jaccard(p, c3)


# In[178]:


jaccard(p, c4)


# In[179]:


jaccard(p, c5)


# In[ ]:




