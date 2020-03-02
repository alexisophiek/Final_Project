from flask import Flask, render_template, redirect, make_response
from flask import jsonify
import pandas as pd
from new_NLTK_clean_and_classify import tweet_list
from nrc_mashup import full_list
import os
import subprocess
import json

# subprocess.call("bin/run_cloud_sql_proxy")

# DB = os.environ.get("DBS_URL")
# conn = psycopg2.connect(DB)
from sqlalchemy import create_engine
# engine = create_engine(DB)
engine = create_engine("postgresql://postgres:dataisgreat@localhost:3306/postgres")
# conn = psycopg2.connect(user = "twitter_app",
#                                   password = "dataistwitter",
#                                   host = "127.0.0.1",
#                                   port = "5432",
#                                   database = "postgres")

# from flask import jsonify
app = Flask(__name__)

''' 
FOR HEROKU - UNCOMMENT
'''
# subprocess.call("bin/run_cloud_sql_proxy")


# cleaned_tweets = []


@app.route("/")
@app.route("/main")
def home():
	return render_template('main.html', title='Twit Stack')

# @app.route("/dump")
# def dump():
# 	return render_template('dump.html')

@app.route("/NRC_lexicon")
def nrcLexicon():
    filepath = "NRC-Sentiment-Emotion-Lexicons/NRC-Emotion-Lexicon-v0.92/NRC-Emotion-Lexicon-Wordlevel-v0.92.txt"
    emolex_df = pd.read_csv(filepath,  names=["word", "emotion", "association"], skiprows=45, sep='\t')
    emolex_words = emolex_df.pivot(index='word', columns='emotion', values='association').reset_index()
    emo = emolex_df.to_json()
    return emo

@app.route("/tweets")
def tweets():
    data = pd.read_sql("select * from tweets", con=engine).to_json(index=False,orient="table")
    tweets = json.loads(data)

    return jsonify(tweets['data'])

# NRC scored DF needs to be returned
@app.route("/NRC_dict")
def get_nrc():
    emo_dict = full_list(tweet_list, emolex_df)
    return emo_dict

# # Returning Cleaned Tweets and NLTK sentiment
# @app.route("/cleaned_tweets")
# def get_cleaned():
#     # tweet_list = get_tweets(conn)
#     # cleaned = clean_tweets(tweet_list)
#     # clean_sent = nltk_sentiment(cleaned)
#     return clean_sent.to_json()

# Word Cloud Return
# @app.route("/word_cloud")
# def get_words():






if __name__ == "__main__":
    app.run(debug=True)
