# Covid Reddit Behaviour

Contributors: Luke Collins, Mel Liow, Nobby Nguyen, Maeve Shi

## Summary

Here we attempt to look into the reddit mental health dataset which contians posts from 28 subreddits(15 mental health support groups) from 2018-2020. We aim to find the impact of COVID-19 on mental health support groups by looking into the data before and after the pandemic. Specifically, we aim to focus the question:  How has the substance use increased over the pandemic?

For the first week, we conducted exploratory data analysis on 30 dataset (15 mental groups, before and after pandemic), which can be found [here](https://github.com/UBC-MDS/covid_reddit_behaviour/tree/eda/eda/subreddit). The exploratory data analysis mainly focus on these parts:

- Features: We explored the features in details by the published paper [here](https://www.jmir.org/2020/10/e22635/.) and decided to only include `substance_use_total`, `subreddit`, `author`, `date`, `post`, and exclude all other features, because they are the only ones relevant to the question. 

- High Level Analysis: We checked if there's any missing values in datasets, as well as what needs to be cleaned. Then we concatenated the pre and post data set to see the difference of descriptive variables.  

- Visualization: We showed the plot of `substance_use_total` distribution before and after the covid to gain a better understanding of our question. 


## Dataset

The datasets we used contains posts and text features for the following timeframes from 15 mental health subreddits: r/EDAnonymous, r/addiction, r/alcoholism, r/adhd, r/anxiety, r/autism, r/bipolarreddit, r/bpd, r/depression, r/healthanxiety, r/lonely, r/ptsd, r/schizophrenia, r/socialanxiety, and r/suicidewatch.

Timeframe: 

- post: Jan 1 to April 20, 2020 (called "mid-pandemic" in manuscript; r/COVID19_support appears). Unique users: 320,364. 
- pre: Dec 2018 to Dec 2019. A full year which provides more data for a baseline of Reddit posts. Unique users: 327,289.

More information can be found [here](https://zenodo.org/record/3941387#.YZl5BC1h1QL)

## Usage
To replicate the analysis, all relevant scripts will be made available in this GitHub repository. All necessarily dependencies will be provided and commands required to fetch the relevant data will be provided as follow. Please run the following commands at the command line/terminal from the `/data` directory of this project after cloning the GitHub repository to your machine.

Navigate to the `/data` directory and run either of the following scripts to download the dataset:
Using python:
```console
$ python download_datasets.py [<output_directory>]
```

Using R:
```console
$ R download_datasets.r [<output_directory>]
```

## License
The source code for the site is licensed under the MIT license, which you can find [here](https://github.com/UBC-MDS/covid_reddit_behaviour/blob/main/LICENSE).
## References
Low D, Rumker L, Talkar T, Torous J, Cecchi G, Ghosh S  
Natural Language Processing Reveals Vulnerable Mental Health Support Groups and Heightened Health Anxiety on Reddit During COVID-19: Observational Study  
Journal of medical Internet research, 22(10), e22635.