from flask import Flask, render_template, redirect, make_response
from flask import jsonify

# from flask import jsonify
app = Flask(__name__)

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
from flask import Flask, render_template, redirect, make_response
# import nltk
# from nltk.tag import pos_tag
# from nltk.stem.wordnet import WordNetLemmatizer
# import re
# import string
# from nltk import FreqDist
# import random
# import psycopg2
# from nltk.tokenize import word_tokenize
import pandas as pd
# import requests
# from nltk import classify
# from nltk import NaiveBayesClassifier
# from nltk.corpus import stopwords
from nltk_modeling import remove_noise, classifier
from nltk_cleaning import clean_tweets, tweet_list, nltk_sentiment

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

@app.route("/cleaned_tweets")
def get_cleaned():
	cleaned_tweets = cleaned.to_json()
	return cleaned_tweets

<<<<<<< HEAD
@app.route("/tweets")
def tweets():
	return render_template('tweets.html')


	# file = os.path.join('application','static','data','CSV_Files', 'combined.csv')

	# return template('dump.html')
=======

   
    
>>>>>>> c5e86f1781a377c9eacfd7f50718185a874478b7
if __name__ == "__main__":
	app.run(debug=True)

	# file = "application/static/data/counties.json"
	# data = county(file)
	# return jsonify(data)