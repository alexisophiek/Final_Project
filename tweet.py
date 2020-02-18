from config import *
import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)
        #Don't know why it doesnt print out coordinates
        print(status.coordinates)


myStreamListener = MyStreamListener()

myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

myStream.filter(track=['election2020'])
