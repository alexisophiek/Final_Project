import nltk
# from nltk.tag import pos_tag
# from nltk.corpus import twitter_samples
from nltk.stem.wordnet import WordNetLemmatizer
# import re, string
from nltk import FreqDist
import random
import psycopg2
# from textblob import TextBlob 
from nltk.tokenize import word_tokenize
import pandas as pd
from nltk.corpus import stopwords
from nltk import classify
stop_words = stopwords.words('english')



p="datasucks"
conn = psycopg2.connect(user = "alexis",
                                  password = f"{p}",
                                  host = "127.0.0.1",
                                  port = "3306",
                                  database = "postgres")

cursor = conn.cursor()


def lemmatize_sentence(tokens):
    lemmatizer = WordNetLemmatizer()
    lemmatized_sentence = []
    for word, tag in pos_tag(tokens):
        if tag.startswith('NN'):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'
        lemmatized_sentence.append(lemmatizer.lemmatize(word, pos))
    return lemmatized_sentence

def remove_noise(tweet_tokens, stop_words = ()):

    cleaned_tokens = []

    for token, tag in pos_tag(tweet_tokens):
        token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'                       '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', token)
        token = re.sub("(@[A-Za-z0-9_]+)","", token)

        if tag.startswith("NN"):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'

        lemmatizer = WordNetLemmatizer()
        token = lemmatizer.lemmatize(token, pos)

        if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
            cleaned_tokens.append(token.lower())
    return cleaned_tokens


def get_all_words(cleaned_tokens_list):
    for tokens in cleaned_tokens_list:
        for token in tokens:
            yield token


def get_tweets_for_model(cleaned_tokens_list):
    for tweet_tokens in cleaned_tokens_list:
        yield dict([token, True] for token in tweet_tokens)


def get_our_tweets(conn):
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
    return tweet_list, folowers

def clean_our_tweets():
    our_tweet_tokens = []
    for each in tweet_list:
        our_tweet_tokens.append(nltk.word_tokenize(each))
    clean_tweet_tokens = []
    for each in our_tweet_tokens:
        clean_tweet_tokens.append(remove_noise(each, stop_words))
    our_words = get_all_words(clean_tweet_tokens)
    return clean_tweet_tokens, our_words

def classify_pickle():
    loaded_model = pickle.load(open(f"notebook/my_classifier.sav", 'rb'))

    tweet = []
    sentiment = []
    for each in clean_tweet_tokens:
        tweet.append(each)
        sentiment.append(loaded_model.classify(dict([token, True] for token in each)))                            





