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
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk_modeling import remove_noise
from nltk_modeling import classifier
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
from config.config import pguser, pw


stop_words = stopwords.words('english')


conn = psycopg2.connect(user = f"{pguser}",
                                  password = f"{pw}",
                                  host = "127.0.0.1",
                                  port = "3306",
                                  database = "postgres")

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

remove_list = [r'@[A-Za-z0-9]+','https?://[A-Za-z0-9./]+','\n','RT :',r'_[A-Za-z0-9]+','  ']

def clean_tweets(remove_list,tweet_list):
    for item in remove_list:
        tweet_list = [re.sub(item,'',tweet) for tweet in tweet_list]
    return tweet_list

cleaned = clean_tweets(remove_list,tweet_list)

#NLTK Sentiment addition to tweets, tweets cleaned but untokenized?
tweet = []
sentiment = []
for each in cleaned:
    custom_tweet = each
    tweet.append(custom_tweet)
    custom_tokens = remove_noise(word_tokenize(custom_tweet))
    sentiment.append(classifier.classify(dict([token, True] for token in custom_tokens)))
                                         
clean_sentiment = pd.DataFrame(tweet, sentiment).reset_index()
clean_sentiment = clean_sentiment.rename(columns = {"index":"NLTK sentiment",0:"tweet"})

print("Dataframe clean_sentiment has been updated")