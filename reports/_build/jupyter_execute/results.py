#!/usr/bin/env python
# coding: utf-8

# # Results
# 
# 

# Using the Wilcoxon rank-sum test from the Python `scipy.stats` library, we can set up our hypotheses for this test as follows:
# 
# $H_0:$ The median number of references to substance abuse per Reddit post is the same in subreddit-specific 'pre-COVID' and 'post-COVID' datasets.
# 
# $H_a:$ The median number of references to substance abuse per Reddit post is **not** the same in subreddit-specific 'pre-COVID' and 'post-COVID' datasets.
# 
# The `scipy.stats` library provided the corresponding p-values for each subreddit. The smaller the p-value, the stronger the evidence against the null hypothesis $H_0$. For a given subreddit, if the p-value is smaller than the predetermined level $\alpha = 0.05$, then there is evidence to reject the null hypothesis in favour of the alternative hypothesis, $H_a$.  
# 
# Our results for each subreddit is as follows:

# In[1]:


import pandas as pd
import os
os.chdir('../analysis')
results = pd.read_csv('stat_tests/stat_tests.csv', index_col=False)

results.columns = ['Subreddit', 'Test statistic', 'p value']
results.style.hide_index()


# We set a standard threshold $\alpha = 0.05$ for statistical significance to compare the p-values for each subreddit. 
# We concluded that _r/adhd_ and _r/lonely_ saw a stistically significant difference between median number of references to substance abuse per reddit-post when comparing the 'pre-COVID' and 'post-COVID' datasets.
# The remaining subreddits tested showed no statistically significant difference between median number of references to substance abuse per reddit-post when comparing the 'pre-COVID' and 'post-COVID' datasets.
