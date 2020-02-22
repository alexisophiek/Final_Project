from config import *
import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
try:
    api.verify_credentials()
    print("Authentication Complete")
except:
    print("Authentication Unable to Complete")


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)
        # Don't know why it doesnt print out coordinates
        print(status.coordinates)


myStreamListener = MyStreamListener()

myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

# Can add multiple tracks
myStream.filter(track=['election2020'],is_async=True)
