# Final_Project

### Data Analytics Boot Camp Final Project, Winter 2020

## Goals:

* Connect to Twitter Streaming API
* View all #Election2020 Tweets
* Run Lists thru a Classifer
* Create Visualizations That Auto-Update

#### Overview to the Process:

* Join Twitter Developer Labs and enable Tweets/Users requests!
* Get a Bearer Token - We are officially in OAuth2.0!
* Pip Install Tweepy in your environment!
* Pip install NLTK
* Model Work
* Google CloudSQL DB Hosting!  Access with SQLAlchemy
* NRC Files Downloaded for Analytical Use
* Heroku finally connected
* Visualize and Play!

## Process Analysis:

For this project, we decided to use the Twitter API, Natural Language Programming, and the NaivesBayes classifier to model and predict overall sentiment for tweets discussing #Election2020.

Admittedly, we struggled with knowing which direction to take a model and how much groundwork would be required to make sure it was accurate.  The world of Natural Language Processing as it pertains to judging sentiment is full of things like linguistic theory, which, as you might guess, comes pre-ordained with biases and historically cemented references to words big and small.  So we limited our scope to what we could easily apply without having to spend hours and hours of doubling check sentiment interpretation...although that is pretty fun.

The goal for our predictions and visualizations was to connect to a Twitter Streaming API call, meaning it would be constantly updating.  This has not been possible yet, but we look forward to pushing for that in the coming weeks. 

So we got connected to twitter...yay.  But how to store it for our calculations and future use.

So we tried some various cleaning, writing out own code to accomplish this.  And as you will, we still wrote a lot of code.  But the benefit of deciding to use NLTK, Natural Language ToolKit, is a lot of the magic of preprocessing that comes with it.

Tools for cleaning: removing noise, removing stop words, tokenizing, POS tagging, and lemmatizing.

NLTK has its own set of corpora called twitter_samples.  For the purpose of modeling, they also supply a positive_tweets.json and a negtaive_tweets.json.
We used NaivesBayes classifier.






### Step One:

Twitter API Access:
* Access Tokens
* Bearer Token
* Streaming API Calls
* Tweets Request

### Step Two:

* Tweet Storing/Cleaning/Handling:
* Structure for cleaned tweets for Database
* What models are going to attempt?
* Cleaning needed to take place with NLTK tools.

### Step Three:

* Model with NLTK Twitter_Samples
* Save Model
* Use Model to Classify #Election2020 Tweets

### Step Three:

* End Points with all Necessary Data
* Back Fill Data with Twitter Search API, before launching Stream (3/1)
* Get beautiful Visualizations attached to stream



