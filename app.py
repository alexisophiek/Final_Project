from flask import Flask, render_template, redirect, make_response
from flask import jsonify
import pandas as pd
from new_NLTK_clean_and_classify import tweet_list
from nrc_mashup import emolex_df, full_list
import os
import subprocess
import json
from sqlalchemy import create_engine

''' 
FOR HEROKU - UNCOMMENT
'''
# subprocess.call("bin/run_cloud_sql_proxy")

# DB = os.environ.get("DBS_URL")
# engine = create_engine(DB)

app = Flask(__name__)

'''
FOR LOCAL - UNCOMMENT
'''
engine = create_engine("postgresql://postgres:dataisgreat@localhost:3306/postgres")


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
	return emo

@app.route("/tweets")
def tweets():
    try:
        data = pd.read_sql("select * from tweets;", con=engine).to_json(index=False,orient="table")
        tweets = json.loads(data)
    
        return jsonify(tweets['data'])

    except:
        print("Error!  It did not work")

# NRC scored DF needs to be returned
@app.route("/NRC_dict")
def get_nrc():
    emo_dict = full_list(tweet_list, emolex_df)
    return jsonify({emo_dict: [emo_dict]})

# # Word Cloud Return
# # @app.route("/word_cloud")
# # def get_words():






if __name__ == "__main__":
    app.run(debug=True)
