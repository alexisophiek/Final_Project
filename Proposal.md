# Twit Predict
### Data Analytics Boot Camp Final Project, Winter 2020


## Twitter Sentiment Analysis

Using the Twitter API, our team will make various insights to the 2020 Elections via Online Engagement, Mentions, and NLP.  We will start by tracking #election2020.


## Rationale 

We want our Audience to have fun looking at the Election of 2020 thru the lense of ML and other Analytics.  A little fun in a dark, dark world.


## Data Sets

We will be using the Twitter API to pull Twitter Objects containing the text of a tweet and the geojson location of that tweet.

[Twitter API documentation](https://developer.twitter.com/en.html)


## Project Stack

* Python Twitter API calls using Tweepy.
* Python connection with SQLAlchmey to PostgreSQL.
* Queries from PostgreSQL, hosted on GoogleSQL Cloud.
* NLTK/NLP for text cleaning and processing.
* NRC for Sentiment Analysis
* ML: Test Models on Number of Interactions per Tweet (breakdown)
* ML: Clustering Test after NLP Processing
* Heat Map with base categories (Long Game Goal)
* Other Visualisations: D3 bar graph of current Moods, WordCloud of most used word, Leader Board of Candidates, and D3 line graph to show mood change over time (with dropdown to specific dates?)


## Project Goals

A long-scroll website containing our whole project presentation, data visualizations, etc.
The GeoTweet Object is inconsistant - Nulls will need to be dropped and then joined with Census GEOJson.  This is not necessary and so will be dropped if we run out of time.

## Work load organization

We will make use of branches and merging branches during our work. Our group will touch base on slack when stuck on something or as a pieces gets finished.  



