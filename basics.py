import psycopg2
import json
from datetime import datetime as dt
import pandas as pd
import re
import nltk
from textblob import TextBlob
nltk.download('stopwords')

from nltk.tokenize import word_tokenize

# import config
# import repo

def find_lexicon_words(grouped_tokens, lexicon_words):
    results = []
    for each in token_master:
        print(each)
        if (each == any(lexicon_words)):
            results.append(this)
#             return i
    print(results)
    return results

print('~ ~ ~ app/logic is starting ~ ~ ~ ~')

# import config

p="dataisok"

conn = psycopg2.connect(user = "sam",
                                  password = f"{p}",
                                  host = "127.0.0.1",
                                  port = "3306",
                                  database = "postgres")
cursor = conn.cursor()

tweet_list = []
followers = []
cursor.execute("select * from tweets")
tweets = cursor.fetchall()
if not tweets:
    print("empty")
for row in tweets:
    for col in row:
        if type(col) is dict:
            tweet_list.append(col['text'])
            followers.append(col['user']['followers_count'])\

#######          ALT method of load tweet_list below

'''
# SAVING A TEXT TWEET_LIST AS A CSV FOR USE LATER

print(type(tweet_list))
tweet_list_df = pd.DataFrame(tweet_list)
tweet_list_df.to_csv('tweet_uncleaned_response.csv')
'''

'''
# LOADING SAID CSV
'''

tweet_list = pd.read_csv('tweet_uncleaned_response.csv')
print('type of read version ', type(tweet_list))


'''
# Twitter organizing
'''

remove_list = [r'@[A-Za-z0-9]+','https?://[A-Za-z0-9./]+','\n','RT :',r'_[A-Za-z0-9]+','  ']

def clean_tweets(remove_list,tweet_list):
    for item in remove_list:
        tweet_list = [re.sub(item,'',tweet) for tweet in tweet_list]
    return tweet_list

# cleaned = clean_tweets(remove_list,tweet_list)
    # len(cleaned)

    # def result(tweet,keyword_list):
    #     if any(word in tweet for word in keyword_list):
    #         return 1
    #     else:
    #         return 0


    # def clean_tweets(remove_list,tweet_list):
    #     for item in remove_list:
    #         tweet_list = [re.sub(item,'',tweet) for tweet in tweet_list]
    #     return tweet_list

cleaned_tweets = clean_tweets(remove_list, tweet_list)

tweets_df = pd.DataFrame(cleaned_tweets)

token_master = []
score_totals_list = []
def tokenize_this_list(cleaned_tweets):

    '''
    list of lists // list of tweets
    '''

    for t in cleaned_tweets:
        '''
        tokens >>> token word list of one tweet
        '''
        tokens = word_tokenize(t)
        
        count = len(tokens)
        score_totals_list.append(count)
        # print('ROW COUNT (tokens)    ',  count)

        token_master.append(tokens)

    print('TOTAL LENGTH OF SCORE TOTALS   ', len(score_totals_list))
    print('TOTAL LENGTH OF TWEETS   ', len(cleaned_tweets))
    print('TOTAL LENGTH OF TOKEN MASTER   ', len(token_master))
    #score_totals_list.to_csv('score_totals_list.csv')
tokenize_this_list(cleaned_tweets)
# score_totals = pd.DataFrame(score_totals_list)
# score_totals.to_csv('score_totals_list.csv')

print('!~!~!~!',len(score_totals_list))
staging_data = pd.DataFrame(cleaned_tweets, token_master, score_totals_list)
# print('TOTAL LENGTH OF TWEETS   ', len(score_totals_list))

print('TOKEN MASTER  - ',len(token_master))

# print(token_master[0])

# TOKEN_MASTER
tokens = token_master

# tokens = tokenize_this_list(cleaned_tweets)

# print(token_master[0])

# df = pd.DataFrame(tweet_list, token_master)
df = pd.DataFrame(
    {'Tweet': cleaned_tweets,
     'TOkens': token_master
    })


df.to_csv('tweet_list_with_tokens.csv')
df.head()
# tweets_df['Tokens'] = tokens
# emolex_words.head()


# NRC
filepath = "NRC-Sentiment-Emotion-Lexicons/NRC-Emotion-Lexicon-v0.92/NRC-Emotion-Lexicon-Wordlevel-v0.92.txt"
emolex_df = pd.read_csv(filepath,  names=["word", "emotion", "association"], skiprows=45, sep='\t')

# print('emolex_df')
emolex_df.head()

# word_list = emolex_df.

# word_list


tokenize_this_list(cleaned_tweets)
emolex_words = emolex_df.pivot(index='word', columns='emotion', values='association').reset_index()
# emolex_words.head(20)

emolex_words.to_csv('emolex_words.csv')



# emolex_words.head(50)

averages = emolex_words.describe()
# print(averages)



# averages
averages.to_csv('averages.csv')


emolex_df.emotion.value_counts()
values = pd.DataFrame(emolex_df.emotion.value_counts())
values.head(20)

# values




emo = emolex_df[(emolex_df.association == 1)].word
print(emo)



# ang = emolex_df[(emolex_df.association == 1) & (emolex_df.emotion == 'anger')].word
# joy = emolex_df[(emolex_df.association == 1) & (emolex_df.emotion == 'joy')].word
# neg = emolex_df[(emolex_df.association == 1) & (emolex_df.emotion == 'negative')].word
# sad = emolex_df[(emolex_df.association == 1) & (emolex_df.emotion == 'sadness')].word
# sur = emolex_df[(emolex_df.association == 1) & (emolex_df.emotion == 'surprise')].word
# tru = emolex_df[(emolex_df.association == 1) & (emolex_df.emotion == 'trust')].word
# ant = emolex_df[(emolex_df.association == 1) & (emolex_df.emotion == 'anticipation')].word
# dis = emolex_df[(emolex_df.association == 1) & (emolex_df.emotion == 'disgust')].word
# fea = emolex_df[(emolex_df.association == 1) & (emolex_df.emotion == 'fear')].word

# print(fea) #id, word

'''
emolex_words =
~~~~~~~
'''
emolex_df[emolex_df.association == 1].emotion.value_counts()


lexicon_words = emolex_words['word'].tolist()
# print(type(lexicon_words))
# type(emolex_df[emolex_df.word == 'charitable'])

results = []
# check_words = ["nice","mean",'asd','final','testhere']

# def find_lexicon_words(grouped_tokens, lexicon_words):
#     results = []
#     for each in token_master:
#         # print(each)
#         if (each == any(lexicon_words)):
#             results.append(this)
# #             return i
# #     print(results)
#     return results

# i = 0
twit_tokens = []

def full_list(token_master,lexicon_words):
    # print('~ ~ ~ ~ ')
    # print(token_master[0])
    # print(token_master[1])
    # print(token_master[2])
    i = 0
    for each in token_master:
        # twit_tokens = []
        i = 0
        single_tokens = each # single tokens is equal to the tokens found in a single tweet 
        # print(single_tokens)
        for e in single_tokens:
            # print(e)
            print('\n\n\n\n\n\n')
            e = [e]
            print(type(e))
            # print(e)
            if e in lexicon_words:
                i += 1
                print('FOUND - ',e)
                twit_tokens.append(e)
                return i, twit_tokens
            print('iiiiiiii', i)
            # print(''twit_tokens)
        return i, twit_tokens
    return i, twit_tokens
# return i, twit_tokens

# return twit_tokens, i
# print(token_master[0])
# full_list(token_master)
print(' - - - - - - - - final. output - - - - - - - - ')
full_list(token_master,lexicon_words)

print(len(twit_tokens))
# print(len(twit_tokens[0]))
print(' - - - - - - - - final. output - - - - - - - - ')
# print(' - - - - - - - - final. output - - - - - - - - ')
# print(' - - - - - - - - final. output - - - - - - - - ')
# print(' - - - - - - - - final. output - - - - - - - - ')
# print(' - - - - - - - - final. output - - - - - - - - ')
# print('202 - ',i)
#         if any(word in check_words for word in word_list):
# #         return 1
#             print(i)
#         results.append(word)
#         if token 
#         word_list result(tweet,keyword_list)
# def sanity(token_master,lexicon_words):
def sanity(a,b,c):

    # remove_list = [r'@[A-Za-z0-9]+','https?://[A-Za-z0-9./]+','\n','RT :',r'_[A-Za-z0-9]+','  ']
    # print(remove_list)
    # br = r'\n'print('')
    # print(br)
    # br = (r'\n' * 3)
    print('\n')
    print(type(a),  '\n', type(b), '\n', 'LEXICON type: ',   type(c))
    # print('CHECK/TOKENS type:    ', type(a),  '~ ~ ~ ~ ~ ' * 40, '  Single Token Record type:   ', type(b) , ' ' * 40, 'LEXICON type: ',  ' ' * 40,  type(c))
    # print(type(check_words))
    # print('__________' * 20)
    # print('LEXICON type: ')
    # print(type(lexicon_words))
    print('first seven...')
    print(lexicon_words[1:7])
    print('~ ~ ~ ~ end of sanity ******')

find_lexicon_words(token_master,lexicon_words)
# sanity(token_master,token_master[0],lexicon_words)

# lexicon_words_testing = ["no","nice","huh","testingg","unique","mean","mean","howdy"]
words_scored = []

# def score_words(grouped_tokens,lexicon_words):
#     words_scored = []
#     print('scoringggggg....')
#     print('    the total length of lexi - ', len(lexicon_words))
#     # print(type(lexicon_words[0]))
#     # print('endlexi')
#     i = 0
#     for tweet_item in grouped_tokens:
#         # print(tweet_item)
#         # print(t)
#         # print(type(t))
#         for t in tweet_item:
#             if t in lexicon_words:
#                 print(t)
#                 i += 1
#                 words_scored.append(t)
#             else:
#                 pass
#             # return t
#     print('~ ~ ~ ~ WORDS SCORED TALLY ~ ~ ~ ~ ')
#     return words_scored
    # print(i)
# score_words(check_words,lexicon_words_testing)
# print(' ~ ~ ~ ~ ~~~ ~ ~ ~ ~ ~ ~. words_scored ~ ~ ~ ~ ~ ~ ','\n',words_scored)
print(len(token_master))
print(len(token_master[1]))
print(token_master[1])

# for each 

# iterate over token_master


score_words(token_master,lexicon_words)
print(' ~ ~ ~ ~ ~~~ ~ ~ ~ ~ ~ ~. words_scored ~ ~ ~ ~ ~ ~ ','\n',words_scored)

print(' ~ ~ scored: ',words_scored)
print(' ~ ~ twit ', twit_tokens)
# print(type(token_master))
# print('   ~~ ~ ~ ~ ~. ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')
# print('   ~~ ~ ~ ~ ~. ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')
# print('   ~~ ~ ~ ~ ~. ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')
# print('   ~~ ~ ~ ~ ~. ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')
# print('   ~~ ~ ~ ~ ~. ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')
# print('   ~~ ~ ~ ~ ~. ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ')
# score_words(token_master,lexicon_words)
# print('lex')
# print(lexicon_words)
# print(words_scored)
