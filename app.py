from flask import Flask, render_template, redirect, make_response
import psycopg2
import pandas as pd
from config.config import pguser, pw
from nltk_modeling import remove_noise
from nltk_cleaning import clean_tweets, get_tweets, nltk_sentiment, generate_tweet_list
from nrc_mashup import create_nrc, full_list

conn = psycopg2.connect(user=f"{pguser}",
                        password=f"{pw}",
                        host="127.0.0.1",
                        port="3306",
                        database="postgres")


app = Flask(__name__)


emolex_df = create_nrc()
tweet_list = get_tweets(conn)
cleaned = clean_tweets(tweet_list)
clean_sent = nltk_sentiment(cleaned)

@app.route("/")
@app.route("/main")
def home():
    return render_template('main.html', title='Twit Stack')


# NRC scored DF needs to be returned
@app.route("/nrc_dict")
def get_nrc():
    # tweet_list = get_tweets(conn)
    # cleaned = clean_tweets(tweet_list)
    # tweets = generate_tweet_list(cleaned)
    # emolex_df = create_nrc()

    emo_dict = full_list(tweets, emolex_df)
    return emo_dict.to_json()

# Returning Cleaned Tweets and NLTK sentiment
@app.route("/cleaned_tweets")
def get_cleaned():
    # tweet_list = get_tweets(conn)
    # cleaned = clean_tweets(tweet_list)
    # clean_sent = nltk_sentiment(cleaned)
    return clean_sent.to_json()

# Word Cloud Return
# @app.route("/word_cloud")
# def get_words():

# @app.route("/dump")
# def dump():
#     # return render_template('dump.html')

@app.route("/NRC_lexicon")
def nrcLexicon():
    # emolex_df = create_nrc()
    emolex_words = emolex_df.pivot(
        index='word', columns='emotion', values='association').reset_index()
    emo = emolex_words.to_json()
    # emo = jsonify(emolex_words)
    return emo

@app.route("/tweets")
def tweets():
    return render_template('tweets.html')



if __name__ == "__main__":
    app.run(debug=True)
