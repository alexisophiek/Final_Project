# Final_Project

### Data Analytics Boot Camp Final Project, Winter 2020

##### Start an Environment for this project called finalproject. Be sure to work in this as we go, so we can keep track of our requirements.* should we have a text environment when we start working with nltk or our chosen sentiment library?

## Step One:

Twitter API

* Access Tokens
* Bearer Token
* Streaming API Calls

DONE!

Info We Want:

* Tweets Request

    -- Place Object - NEEDED!   Will require that we throw out NULL objects if we do.

    -- Tweet Object - DONE!

## Step Two:

Tweet Storing/Cleaning/Handling:

Structure for cleaned DF for Database:
date, place, user, text, metadata (everything else?)

* NLTK
* Train/Test/Run?

DB Connection:

* PostgreSQL

 -- intialize 
 -- load
 -- call endpoint

 ## Step Three:
 Build Framework for WebApp
 Play with ML!
 Build Visualizations
 -- Need to add create database not just tables to database_setup.py


 ## Set Up:

* Join Twitter Developer Labs and enable Tweets/Users requests!
* Get a Bearer Token - We are officially in OAuth2.0!
* Pip Install Tweepy in your environment!
* Pip install NLTK - do we want Text Blob?
* Google SQL Hosting!
* NRC!


* cloud_sql_proxy -instances=data-class-1570673095864:us-west1:twitter-db=tcp:3306
* count of tweets by day- running line graph for mapping total activity.
* twitter search for top 4 candidates and see how many retweets per day they have?