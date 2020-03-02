import tweepy
from config.config import consumer_secret, consumer_key, access_token_secret, access_token
import datetime as dt
import json
import psycopg2

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
try:
    api.verify_credentials()
    print("Authentication Complete")
except:
    print("Authentication Unable to Complete")

conn = psycopg2.connect(user = "alexis",
                                  password = "datasucks",
                                  host = "127.0.0.1",
                                  port = "3306",
                                  database = "postgres")
cursor = conn.cursor()
    
start_date = (dt.datetime.now() - dt.timedelta(days=7)).strftime("%Y-%m-%d")
end_date = (dt.datetime.now() - dt.timedelta(days=6)).strftime("%Y-%m-%d")


counter = 0

print(f"Tweet Added number {counter}")

tweets = tweepy.Cursor(api.search, q='#election2020', rpp=100, since=start_date, until=end_date).items()
for tweet in tweets:
    counter +=1
    followers = tweet.user.followers_count
    tweet_id = tweet.id
    user_id = tweet.user.id
    statuses = tweet.user.statuses_count
    entities = tweet.entities
    sn = tweet.user.screen_name
    date = tweet.created_at.strftime('%Y-%m-%d %H:%M:%S')
    text = tweet.text
    
#     CREATE TABLE new_tweets (date date, tweet_id bigint, user_id bigint, username text, statuses_count int, follower_count int, entities text, tweet_text text);
    cursor.execute("INSERT INTO new_tweets (date, tweet_id, user_id, username, statuses_count, follower_count, entities, tweet_text) \
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);", (tweet.created_at.strftime('%Y-%m-%d %H:%M:%S'), tweet_id, user_id, sn, statuses, followers,json.dumps(entities), text))
    conn.commit()
    print(f"Tweet Added number {counter}")    
    
cursor.close()
conn.close()