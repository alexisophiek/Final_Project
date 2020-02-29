from config import *
import tweepy
import datetime as dt

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

two_days = (dt.datetime.now() - dt.timedelta(days=2)).strftime("%Y-%m-%d")
one_day = (dt.datetime.now() - dt.timedelta(days=1)).strftime("%Y-%m-%d")

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
try:
    api.verify_credentials()
    print("Authentication Complete")
except:
    print("Authentication Unable to Complete")

MAX_TWEETS = 300

tweets = tweepy.Cursor(api.search, q='#election2020', rpp=100, since=two_days, until=one_day).items(MAX_TWEETS)

followers_count = []
interaction_count = []
for tweet in tweets:
    interaction = tweet.retweet_count + tweet.favorite_count
    interaction_count.append(interaction)
    followers_count.append(tweet.user.followers_count)
    # print(tweet.text)
    # print(tweet.user.followers_count)
    # print(tweet.retweet_count)
    # print(tweet.favorite_count)

    pass

