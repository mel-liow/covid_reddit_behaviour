# Methodology

In order to investigate how substance use on Reddit has changed over the pandemic, we first introduce the dataset and conduct an exploratory data analysis (EDA) on several subreddit datasets.
## Data set
The datasets, obtained from a public data resource, is called the [Reddit mental health dataset](https://zenodo.org/record/3941387#.YZl5BC1h1QL), and has been previously processed and organised by Low et al {cite:p}`low2020natural`. The data includes Reddit posts from 826,961 unique users from 2018 to 2020. They provide two CSV files for each period - _before_ (2018-2019) and _during_ (2020) the pandemic - for 15 different subreddits. 

Each observation is a Reddit user's post - a message written on a specific subreddit - which has been processed to extract features that are common in NLP. 

The feature extractions are as follows (n is the number of columns):
- Linguistic inquiry and word count (LIWC) (n=62);
- Sentiment analysis (n=4); 
- Basic word and syllable counts (n=8); 
- Punctuation (n=1); 
- Readability metrics (n=9); 
- Term frequency–inverse document frequency (TF-IDF) ngrams (256-1024) to capture words and phrases that characterize specific posts; 
- Manually built lexicons about suicidality (n=1), economic stress (n=1), isolation (n=1), substance use (n=1), domestic stress (n=1), and guns (n=1). 

Alongside these features include:
- Author (Reddit user name)
- Date
- Post

For this specific study, we have discarded most of these features from the dataset as they are unrelated to the question in focus. Even though understanding the sentiment of the posts over the pandemic is cruicial to developing a narrative, most of this work has already been conducted by Low et al {cite:p}`info:doi/10.2196/22635`. 
Instead, we have selected one of the text-derived metrics available in this dataset, _substance_abuse_total_, as the focus metric. This value is calculated as the number of references to substance abuse in a Reddit user's post and is a feature that we will use to compare across the _before_ and _during_ pandemic datasets for each subreddit.

Our final processed data sets contained the following features:

- author
- date
- subreddit
- post
- period
- substance_use_total
## Data processing
We used the Python programming language {cite:p}`pypi` and the Pandas library {cite:p}`pandas` to perform the data reading and processing. We automated this process by writing two Python scripts - one that downloads the raw datasets and another that renames columns and reduces the data to the columns of interest. Additionally, we combined the _before_ and _during_ pandemic data sets and introduced a new column _period_ to distinguish between the two time frames. This helped to represent the data better and allow us to easily compare the timeframes when conducting the exploratory analysis.
## Data Analysis

[pic of eda to show distribution of data for a few subreddits]

Deciding which test statistic to use when performing hypothesis tests depends on the distribution of the data and its characteristics. Given that the distribution of `substance_use_total` is skewed, we decided to use the median as oppose to the mean for our test estimator.

Moreover, from the data analysis we saw that there was a data imbalance based on the time of data collection. The data for the _before_ pandemic posts spans 11 months whereas the data at the point of collection only makes 3 months of the _during_ pandemic posts available for use. The unequal-sized data sets for each `period` therefore allowed us to determine the Wilcoxon rank-sum statistic as a suitable test statistic.

The Wilcoxon rank-sum statistic is used to compare two independent samples to assess whether their population median ranks differ.

Wilcoxon rank-sum test is used to compare two independent samples, while Wilcoxon signed-rank test is used to compare two related samples, matched samples, or to conduct a paired difference test of repeated measurements on a single sample to assess whether their population mean ranks differ.

We performed hypothesis tests with a significance level of $\alpha = 0.05$, to determine which subreddits had a statistically significant difference in median number of references to substance abuse over the two time frames. The results are shown in the next section.
