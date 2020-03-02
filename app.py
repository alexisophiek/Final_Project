from flask import Flask, render_template, redirect, make_response
from flask import jsonify
import pandas as pd
from new_NLTK_clean_and_classify import tweet_list, cleaned_df, classify_pickle, clean_tweet_tokens
from nrc_mashup import full_list
import os
import subprocess
import json
from wordCloud import get_word_cloud
from sqlalchemy import create_engine


''' 
FOR HEROKU - UNCOMMENT
'''
# subprocess.call("bin/run_cloud_sql_proxy")


# DB = os.environ.get("DBS_URL")
# conn = psycopg2.connect(DB)
# from sqlalchemy import create_engine
engine = create_engine("postgresql://postgres:dataisgreat@localhost:3306/postgres")



app = Flask(__name__)



@app.route("/")
@app.route("/main")
def home():
	return render_template('main.html', title='Twit Stack')

@app.route("/model")
def model():
	return render_template('NLTK_Model_Slides.slides.html', title='Twit Model')


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
    print(type(tweets))
    return tweets


    return jsonify(tweets['data'])

# NRC scored DF needs to be returned
@app.route("/NRC_dict")
def get_nrc():
    filepath = "NRC-Sentiment-Emotion-Lexicons/NRC-Emotion-Lexicon-v0.92/NRC-Emotion-Lexicon-Wordlevel-v0.92.txt"
    emolex_df = pd.read_csv(filepath,  names=["word", "emotion", "association"], skiprows=45, sep='\t')
    emo_dict = full_list(tweet_list, emolex_df)
    return json.dumps(emo_dict, indent=4)

@app.route("/cleaned_tweets")
def get_cleaned():
    return cleaned_df.to_html()

# Word Cloud Return
@app.route("/word_cloud")
def get_words():
    cloud = get_word_cloud()
    return json.dumps(cloud)





if __name__ == "__main__":
    app.run(debug=True)
