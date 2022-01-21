# Conclusion

We conducted a statistical analysis on data gathered from multiple subreddits to answer an inferential question on whether the number of substance abuse references per user post increased during the COVID-19 pandemic on Reddit.

The hypothesis tests for each subreddit were presented in a [table](results.md) alongside their corresponding p-values. A p-value less than 0.05 indicated that there was statistical evidence that the median number of references to substance abuse per post had changed since before the pandemic.

We conclude that only two subreddits, _r/adhd_ and _r/lonely_ showed statistically siginificant difference. Accordingly, we reject the null hypothesis in favour of the alternative hypothesis - i.e that in these subreddits, the median number of references to substance abuse per Reddit-post _has_ changed between the time before the pandemic and during.
## Further work
There is room for improving the justifications of using the Wilcoxon rank-sum test for this particular dataset. From further investigation, it may be inappropritate to use this particular test statistic given that the Wilcoxon rank-sum works best for ordinal and paired data {cite:p}`XIA2020309`. Therefore further work includes a reassessment on using this particular method and instead deduce a more appropriate test statistic to conduct the hypothesis tests.

Additionally, the scope of this report only reveals the frequency of substance use related words per Reddit post. It does not delve further into more contextual significant meaning - i.e. we do not explore whether this metric is correlated to a rise in substance abuse or the _effect_ it has on Reddit users. This is open research that is also mentioned in the paper by Low et al. 

However, this report opens up more avenues in terms of the methodology used to explore trends in online behaviours. Given the ease of automating the data processing and analysis using Python, conducting a statistical test to investigate the significance of differences in behaviours _before_ and _during_ the COVID-19 pandemic is accessible to many researchers and those interested in the field. We have provided a research "template" and methodology as a foundation that can be built upon and improved to help further investigate the effects of the COVID-19 pandemic on online users. 

