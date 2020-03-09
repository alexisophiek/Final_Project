from flask import Flask, render_template, redirect, make_response
from flask import jsonify
import pandas as pd
from new_NLTK_clean_and_classify import tweet_list, cleaned_df, classify_pickle, clean_tweet_tokens
from nrc_mashup import full_list
import os
import subprocess
import json
from sqlalchemy import create_engine

myDict = {} 

''' 
FOR HEROKU - UNCOMMENT
'''
subprocess.call("bin/run_cloud_sql_proxy")


DB = os.environ.get("DBS_URL")
engine=create_engine(DB)

# engine = create_engine("postgresql://sam:dataisok@localhost:3306/postgres")



app = Flask(__name__)


# Web Page
@app.route("/")
@app.route("/main")
def home():
	return render_template('main.html', title='Twit Stack')

@app.route('/tracked')
def tracked():
    tracked = {'emotions': ["anger", "anticipation", "disgust", "fear", "joy", "sadness", "surprise", "trust"],'sentiment':["negative", "positive"]}
    return tracked
# IPYNB NOTEBOOk
@app.route("/model")
def model():
	return render_template('NLTK_Model_Slides.slides.html', title='Twit Model')

## Straight Up Lexicon
@app.route("/NRC_lexicon")
def nrcLexicon():
    filepath = "NRC-Sentiment-Emotion-Lexicons/NRC-Emotion-Lexicon-v0.92/NRC-Emotion-Lexicon-Wordlevel-v0.92.txt"
    emolex_df = pd.read_csv(filepath,  names=["word", "emotion", "association"], skiprows=45, sep='\t')
    emolex_words = emolex_df.pivot(index='word', columns='emotion', values='association').reset_index()
    emo = emolex_df.to_json()
    return emo

# Old DB Stream
@app.route("/tweets")
def tweets():
    data = pd.read_sql("select * from tweets", con=engine).to_json(index=False,orient="table")
    tweets = json.loads(data)
    return tweets

# New DB Backfilled with 7 days
@app.route("/new_tweets")
def new_tweets():
    data = pd.read_sql("select * from new_tweets", con=engine)
    return data.to_json()

@app.route("/cleaned_tweets")
def get_cleaned():
    clean_list = []
    for i,row in cleaned_df.iterrows():
        clean_list.append({"Tweet Tokens":cleaned_df['Tokens'].iloc[i],"Sentiment":cleaned_df['Emotions'].iloc[i]})
    return jsonify(clean_list)

# End Point for Word Cloud Vis
@app.route("/word_cloud")
def get_words():
    my_list = []
    cloud = pd.read_sql("select * from word_cloud",con=engine)
    for i,row in cloud.iterrows():
        my_list.append({'x':cloud['word'].iloc[i],'value':int(cloud['value'].iloc[i]), 'category':cloud['category'].iloc[i]})
    return jsonify(my_list)


@app.route('/emotions_and_tweets')
def emo_tweets():
    d = pd.read_sql("select * from emotions LIMIT 300", con=engine).to_json(index=False,orient="table")
    print(len(d))
    # data = pd.read_sql("select * from emotions where length(emotions.data.emotion_disctionaries) >2 ", con=engine).to_json(index=False,orient="table")
    # data = d[1]
    return d

# NRC Table Emotions
@app.route('/df_from_sql')
def dfSSql():
     d = pd.read_sql_table("emotions",con=engine)
     # d = sql_DF[emotion_dictionaries]
     d = d[0]
     print(type(d))
     print(d)
     dfjson = d.to_json()
     return dfjson


if __name__ == "__main__":
    app.run(debug=True)
