# Methodology

We look into the [Reddit mental health dataset](https://zenodo.org/record/3941387#.YZl5BC1h1QL) produced by [...]() from which they have selected 15 mental-health-specific subreddit datasets for EDA. These datasets contain collections of Reddit user posts from 2018-2020, and have already beem split into pre-pandemic and post-pandemic. 



## Data set

The datasets were originally obtained from [https://www.jmir.org/2020/10/e22635/](https://www.jmir.org/2020/10/e22635/). They provide us with two CSV files, for each period (pre and post pandemic), for 15 different subreddits. 

Each observation is a Reddit user's post - a message written on a specific subreddit - which has been processed to extract features that are common in natural language processing [cite TO PAPER]. 

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


## 