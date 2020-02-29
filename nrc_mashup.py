
def tokenize_this_list(text):
    token_list = []
    token_count = []
    for each in text:
        tokens = word_tokenize(each)
        count = len(tokens)
        token_list.append(tokens)
        token_count.append(count)
    return token_count, token_list

token_count, token_list = tokenize_this_list(tweet)

print('Length of Token_Count =' + str(len(token_count)))
print('Length of Token_List =' + str(len(token_list)))

# NRC
filepath = "NRC-Sentiment-Emotion-Lexicons/NRC-Emotion-Lexicon-v0.92/NRC-Emotion-Lexicon-Wordlevel-v0.92.txt"
emolex_df = pd.read_csv(filepath,  names=["word", "emotion", "association"], skiprows=45, sep='\t')
emolex_words = emolex_df.pivot(index='word', columns='emotion', values='association').reset_index()




def full_list(token_list, df):
    # Set list to hold dictionary and return
    emo_list = []
    # Loop through tweets in list
    for tweet in token_list:
        # Set dictionary to hold emotions as keys and their counts as values
        lexi_dict = {}
        # Loop through words in tweet
        for word in tweet:
            # Check if word is in df -> emotion lexicon dataframe (emolex_df) in our example
            if word in df.word.to_list():
                # List to hold index where association column is 1
                assoc = []
                # Get indices where word from tweet is in df
                i = df.index[df['word'] == word]
                for index in i:
                    # Check if association is 1 (not 0) and append to list
                    if df['association'].iloc[index] == 1:
                        assoc.append(index)
                    # Where the word from tweet has association = 1, add to dict if not there, or update count if there
                    for j in assoc:
                        emo = df['emotion'].iloc[j]
                        if (emo in lexi_dict.keys()):
                            lexi_dict[emo] += 1
                        else:
                            lexi_dict[emo] = 1
        # Append to list
        emo_list.append(lexi_dict)
    # return list
    return emo_list

emotion_list = full_list(token_list,emolex_df)
               
print(emotion_list[:10])









# new = clean_sentiment.groupby("sentiment")["sentiment"].count()

# REFACTOR INTO LOOP FOR EACH KEY WORD OR CANDIDATE
# bernie = []
# warren = []
# buttigeig =[] 
# biden = []
# bloomberg = [] 
# trump = []


# for tweet in clean_sentiment:
#     if tweet == 'pete|buttigieg':
#         buttigeig.append(tweet)

# buttigieg = clean_sentiment[clean_sentiment['tweet'].str.contains('pete|buttigieg', case = False)]
# buttigieg_count = buttigieg.groupby("sentiment")["sentiment"].count()
# buttigieg_count


# biden = clean_sentiment[clean_sentiment['tweet'].str.contains('joe|biden', case = False)]
# biden_count = biden.groupby("sentiment")["sentiment"].count()
# biden_count

# trump = clean_sentiment[clean_sentiment['tweet'].str.contains('donald|trump', case = False)]
# trump_count = trump.groupby("sentiment")["sentiment"].count()
# trump_count

# bernie = clean_sentiment[clean_sentiment['tweet'].str.contains('bernie|sanders', case = False)]
# bernie_count = bernie.groupby("sentiment")["sentiment"].count()
# bernie_count


