from flask import Flask, render_template, redirect, make_response
from flask import jsonify

# from flask import jsonify
app = Flask(__name__)

import psycopg2
# from nltk.tokenize import word_tokenize
import pandas as pd
from config import pguser, pw # import config
# from config.config import pguser, pw


from nltk_modeling import remove_noise
from nltk_cleaning import clean_tweets, get_tweets, nltk_sentiment


conn = psycopg2.connect(user = f"{pguser}",
                                password = f"{pw}",
                                host = "127.0.0.1",
                                port = "3306",
                                database = "postgres")

import nltk_modeling
import nltk
from nltk.tag import pos_tag
from nltk.corpus import twitter_samples
from nltk.stem.wordnet import WordNetLemmatizer
import re, string
from nltk import FreqDist
import random
import psycopg2
from textblob import TextBlob 
from nltk.tokenize import word_tokenize
import pandas as pd
import requests
import nltk_cleaning
from nltk import classify
from nltk import NaiveBayesClassifier
from nltk.corpus import stopwords
# import jsonify


cleaned_tweets = []

@app.route("/")
@app.route("/main")
def home():
	return render_template('main.html', title='Twit Stack')
# @app.route("/tweets")
# def tweets():
# 	pass
# 	# return render_template('main.html', title='Twit Stack')

@app.route("/dump")
def dump():
	return render_template('dump.html')

@app.route("/NRC_lexicon")
def nrcLexicon():
	filepath = "NRC-Sentiment-Emotion-Lexicons/NRC-Emotion-Lexicon-v0.92/NRC-Emotion-Lexicon-Wordlevel-v0.92.txt"
	emolex_df = pd.read_csv(filepath,  names=["word", "emotion", "association"], skiprows=45, sep='\t')
	emolex_words = emolex_df.pivot(index='word', columns='emotion', values='association').reset_index()
	emo = emolex_words.to_json()
	# emo = jsonify(emolex_words)
	return emo

# @app.route("/cleaned_tweets")
# def get_cleaned():
# 	cleaned_tweets = cleaned.to_json()
# 	return cleaned_tweets

# @app.route("/cleaned_tweets")
# def get_cleaned():
# 	cleaned_tweets = cleaned.to_json()
# 	return cleaned_tweets

@app.route("/tweets")
def tweets():
	return render_template('tweets.html')
   

@app.route("/cleaned_tweets")
def get_cleaned():
    tweet_list = get_tweets(conn)
    cleaned = clean_tweets(tweet_list)
    clean_sent = nltk_sentiment(cleaned)
    return clean_sent.to_json()



if __name__ == "__main__":
	app.run(debug=True)

	# file = "application/static/data/counties.json"
	# data = county(file)
	# return jsonify(data)