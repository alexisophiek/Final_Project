import pandas as pd
import nltk
from nltk.corpus import stopwords
import string
import re
from nltk.tokenize import word_tokenize
import os
from political_words import words
stopwords = set(stopwords.words('english'))
from sqlalchemy import create_engine

''' 
FOR HEROKU - UNCOMMENT
'''
# DB = os.environ.get("DBS_URL")
# engine = create_engine(DB)

'''
FOR LOCAL USE - UNCOMMENT
'''
engine = create_engine("postgresql://alexis:datasucks@localhost:3306/postgres")


def get_word_cloud():
    data =pd.read_sql("select * from new_tweets",con=engine)

    tweet_list = data['tweet_text'].to_list()
    tokenized = [word_tokenize(tweet) for tweet in tweet_list]
    emoji_pattern = re.compile("["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            "]+", flags=re.UNICODE)

    filtered_tweets = []
    for tweet in tokenized:
        filtered_tweet = []
        for word in tweet:
            if word.lower() not in stopwords and word not in string.punctuation and emoji_pattern.sub(r'', word):
                filtered_tweet.append(emoji_pattern.sub(r'', word.lower()))
        filtered_tweets.append(filtered_tweet)


    word_count = {}
    for tweet in filtered_tweets:
        for word in tweet:
            if word.lower() in word_count.keys():
                word_count[word.lower()] += 1
            else:
                word_count[word.lower()] = 1

    word_list_counts = {key:value for key, value in word_count.items() if key.lower() in words}

    filepath = "NRC-Sentiment-Emotion-Lexicons/NRC-Emotion-Lexicon-v0.92/NRC-Emotion-Lexicon-Wordlevel-v0.92.txt"
    emolex_df = pd.read_csv(filepath,  names=["word", "emotion", "association"], skiprows=45, sep='\t')

    my_list = []
    for key in word_list_counts.keys():
        my_dict = {}
        my_dict['x'] = key
        my_dict['value'] = word_list_counts[key]
        lexi_dict = {}
        if key in emolex_df.word.to_list():
            assoc = []
            i = emolex_df.index[emolex_df['word'] == key]
            for index in i:
                if emolex_df['association'].iloc[index] == 1:
                    assoc.append(index)
                for j in assoc:
                    emo = emolex_df['emotion'].iloc[j]
                    if (emo in lexi_dict.keys()):
                        lexi_dict[emo] += 1
                    else:
                        lexi_dict[emo] = 1
        print(lexi_dict)
        if not (lexi_dict):
            max_key = 'none'
        else:
            max_key = max(lexi_dict, key=lambda k: lexi_dict[k])
        print(max_key)
        my_dict['category'] = max_key
        my_list.append(my_dict)

    return my_list


my_list = get_word_cloud() 
