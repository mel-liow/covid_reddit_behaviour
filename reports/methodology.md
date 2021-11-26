# Methodology

In order to investigate how substance use on Reddit has changed over the pandemic, we first conduct an exploratory data analysis (eda) on several Reddit datasets described below.
## Data set

The datasets were obtained from [Reddit mental health dataset](https://zenodo.org/record/3941387#.YZl5BC1h1QL), a dataset processed and organised by Low et al {cite:p}`low2020natural`. They provide us with two CSV files, for each period (pre and post pandemic), for 15 different subreddits. 

Each observation is a Reddit user's post - a message written on a specific subreddit - which has been processed to extract features that are common in natural language processing.

The feature extractions are as follows:
- LIWC (n=62);
- sentiment analysis (n=4); 
- basic word and syllable counts (n=8); 
- punctuation (n=1); 
- readability metrics (n=9); 
- term frequency–inverse document frequency (TF-IDF) ngrams (256-1024) to capture words and phrases that characterize specific posts; 
- manually built lexicons about suicidality (n=1), economic stress (n=1), isolation (n=1), substance use (n=1), domestic stress (n=1), and guns (n=1). 

Alongside these features include:
- Reddit user name
- Date of post
- 


## Data cleaning

Nobby to write about data cleaning...
- what we did
- what we could have done further 
- feature engineering? create new features?
- 

## Data analysis
To help familiarise the reader with the data, we present a more in depth analysis of the features and highlight any interesting trends. This can be found in the [data analysis](TODO) section.

We perform a statistical test and report the findings in the [results]() section. 
