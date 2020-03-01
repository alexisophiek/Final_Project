from flask import Flask, render_template, redirect, make_response
from flask import jsonify

app = Flask(__name__)

import psycopg2
import pandas as pd
from config import pguser, pw

from nltk_cleaning import get_tweets, clean_tweets, nltk_sentiment
# from nltk_cleaning import clean_tweets, get_tweets, nltk_sentiment
import numpy as np

import matplotlib.pyplot as plt


conn = psycopg2.connect(user = f"{pguser}",
                                password = f"{pw}",
                                host = "127.0.0.1",
                                port = "3306",
                                database = "postgres")

import nltk_modeling
import nltk
from nltk.tag import pos_tag
# from nltk.corpus import twitter_samples
from nltk.stem.wordnet import WordNetLemmatizer
import re, string
from nltk import FreqDist
import random
import psycopg2
from textblob import TextBlob 
from nltk.tokenize import word_tokenize
import pandas as pd
import requests
from nltk import classify
from nltk import NaiveBayesClassifier
from nltk.corpus import stopwords

cleaned_tweets = []

@app.route("/")
@app.route("/main")
def home():

	return render_template('main.html', title='Twit Stack')

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


@app.route('/vis')
def vis():

	return render_template('visual.html')

'''
@app.route("/tweets")

	def tweets():
	return cleaned_tweets.to_json()
	return render_template('tweets.html')
'''
# tweet_list = get_tweets(conn)
# cleaned = clean_tweets(tweet_list)

conn = psycopg2.connect(user = "sam",
                                  password = "dataisok",
                                  host = "127.0.0.1",
                                  port = "3306",
                                  database = "postgres")

@app.route("/get_tweets")
def tweets():
	conn = psycopg2.connect(user = "sam",password = "dataisok",host = "127.0.0.1",port = "3306",database = "postgres")
	tweet_list = get_tweets(conn)
	cleaned = clean_tweets(tweet_list)
	# head = cleaned.head(30)
	desc = cleaned.describe()
	print(desc)
	print('length of cleaned tweet list is... ',len(cleaned))
	print(type(cleaned))
	clean_sent = nltk_sentiment(cleaned)
	return clean_sent.to_json()
if __name__ == "__main__":
	app.run(debug=True)

	# file = "application/static/data/counties.json"
	# data = county(file)
	# return jsonify(data)