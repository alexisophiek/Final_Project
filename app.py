from flask import Flask, render_template, redirect, make_response
# import nltk
# from nltk.tag import pos_tag
# from nltk.stem.wordnet import WordNetLemmatizer
# import re
# import string
# from nltk import FreqDist
# import random
import psycopg2
# from nltk.tokenize import word_tokenize
import pandas as pd
from config.config import pguser, pw

# import requests
# from nltk import classify
# from nltk import NaiveBayesClassifier
# from nltk.corpus import stopwords
from nltk_modeling import remove_noise
from nltk_cleaning import clean_tweets, get_tweets, nltk_sentiment


conn = psycopg2.connect(user = f"{pguser}",
                                password = f"{pw}",
                                host = "127.0.0.1",
                                port = "3306",
                                database = "postgres")



app = Flask(__name__)


@app.route("/")
@app.route("/main")
def home():
    return render_template('main.html', title='Twit Stack')


@app.route("/cleaned_tweets")
def get_cleaned():
    tweet_list = get_tweets(conn)
    cleaned = clean_tweets(tweet_list)
    clean_sent = nltk_sentiment(cleaned)
    return clean_sent.to_json()


if __name__ == "__main__":
    app.run(debug=True)

