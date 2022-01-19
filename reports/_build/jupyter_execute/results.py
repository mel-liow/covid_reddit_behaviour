#!/usr/bin/env python
# coding: utf-8

# # Results
# 
# 

# Using the Wilcoxon rank-sum test, we can set up our hypotheses for this test as follows:
# 
# $H_0:$ The median number of references to substance abuse per reddit-post is the same in subreddit-specific 'pre-COVID' and 'post-COVID' datasets.
# 
# $H_a:$ The median number of references to substance abuse per reddit-post is **not** the same in subreddit-specific 'pre-COVID' and 'post-COVID' datasets.
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
