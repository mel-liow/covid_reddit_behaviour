# Methodology

In order to investigate how substance use on Reddit has changed over the pandemic, we first introduce the dataset and conduct an exploratory data analysis (EDA) on several subreddit datasets.
## Data set
The datasets, obtained from a public data resource, is called the [Reddit mental health dataset](https://zenodo.org/record/3941387#.YZl5BC1h1QL), and has been previously processed and organised by Low et al {cite:p}`low2020natural`. They provide two CSV files for each period - pre (2018-2019) and post (2019-2020) pandemic - for 15 different subreddits. 

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
## Data processing
We used the Python programming language {cite:p}`pypi` and the Pandas library {cite:p}`pandas` to perform the data reading and processing. We automated this process by writing two Python scripts - one that downloads the raw datasets and another that renames columns and reduces the data to the columns of interest. Additionally, we combined the 'pre' and 'post' pandemic data sets and introduced a new column _period_ to distinguish between the two time frames. This helped to represent the data better and allows us to easily compare the timeframes when conducting the exploratory analysis.

We selected one of the text-derived metrics available in this dataset, _substance_abuse_total_, as the focus of our study. This value is calculated as number of references to substance abuse in a Reddit user's post and is a feature that we will use to compare across the 'pre' and 'post' pandemic datasets for each subreddit.

Our final processed data sets contained the following features:

- author
- date
- subreddit
- post
- period
- substance_use_total

## Data Analysis



## Hypothesis testing using Wilcoxon rank-sum statistic
For each subreddit data set we computed the Wilcoxon rank-sum statistic and compared the median number of references to substance abuse per Reddit post.

The Wilcoxon rank-sum statistic (also referred to as the Mann-Whitney-Wilcoxon rank-sum) 

Given the data imbalance of each data set where there are unequal-sized samples for each _period_, the Wilcoxon rank-sum statistic lends itself to be more a better test statistic.