import nltk
import re, string
import random
import psycopg2
import pandas as pd
from nltk import FreqDist
from nltk import classify
from nltk import NaiveBayesClassifier
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk_modeling import remove_noise, modeling

def get_tweets(conn):
    cursor = conn.cursor()
    tweet_list = []
    followers = []
    cursor.execute("select * from tweets")
    tweets = cursor.fetchall()
    if not tweets:
        print("empty")
    for row in tweets:
        for col in row:
            if type(col) is dict:
                tweet_list.append(col['text'])
                followers.append(col['user']['followers_count'])
    return tweet_list

<<<<<<< HEAD
# def clean_tweets(remove_list,tweet_list):
#     for item in remove_list:
#         tweet_list = [re.sub(item,'',tweet) for tweet in tweet_list]
#     return tweet_list

# cleaned = clean_tweets(remove_list,tweet_list)

=======
>>>>>>> 7ea802d618ee76f49a2e4023e963a88a79fc1e7a
def clean_tweets(tweet_list):
    remove_list = [r'@[A-Za-z0-9]+','https?://[A-Za-z0-9./]+','\n','RT :',r'_[A-Za-z0-9]+','  ']
    for item in remove_list:
        tweet_list = [re.sub(item,'',tweet) for tweet in tweet_list]
    return tweet_list
<<<<<<< HEAD
#NLTK Sentiment addition to tweets, tweets cleaned but untokenized?
def nltk_sentiment(cleaned):
    tweet = []
    sentiment = []
    for each in cleaned:
        custom_tweet = each
        tweet.append(custom_tweet)
        custom_tokens = remove_noise(word_tokenize(custom_tweet))
        sentiment.append(classifier.classify(dict([token, True] for token in custom_tokens)))
        clean_sentiment = pd.DataFrame(tweet, sentiment).reset_index()
        clean_sentiment = clean_sentiment.rename(columns = {"index":"NLTK sentiment",0:"tweet"})
    return clean_sentiment
print("Cleaning Utility is Ready")
=======
>>>>>>> 7ea802d618ee76f49a2e4023e963a88a79fc1e7a

#NLTK Sentiment addition to tweets, tweets cleaned but untokenized?
def nltk_sentiment(cleaned):
    tweet = []
    sentiment = []
    for each in cleaned:
        custom_tweet = each
        tweet.append(custom_tweet)
        custom_tokens = remove_noise(word_tokenize(custom_tweet))
        sentiment.append(classifier.classify(dict([token, True] for token in custom_tokens)))
                                         
        clean_sentiment = pd.DataFrame(tweet, sentiment).reset_index()
        clean_sentiment = clean_sentiment.rename(columns = {"index":"NLTK sentiment",0:"tweet"})
    return clean_sentiment

print("Cleaning Utility is Ready")