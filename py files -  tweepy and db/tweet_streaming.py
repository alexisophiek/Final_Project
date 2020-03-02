from config.config import consumer_key,consumer_secret,access_token,access_token_secret
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


    def on_data(self, data):
        print("On Data")
        all_data = json.loads(data)
        date = all_data['created_at']
        place = all_data['user']['location']
        tweet = all_data["text"].replace('"', "")
        username = all_data["user"]["screen_name"]
        metadata = all_data['user']["favourites_count"]
        print(date)
        print((place, username, tweet))
        self.num_tweets += 1
        if self.num_tweets < 500:
            cursor.execute('INSERT INTO twitter_feed (date, user_location, user_id, text, metadata) VALUES (%s,%s,%s,%s,%s);', (dt.strptime(
                date, '%a %b %d %H:%M:%S %z %Y').strftime('%Y-%m-%d %H:%M:%S'), place, tweet, username, metadata))

            cursor.execute('INSERT INTO tweets (data) VALUES (%s);',
                           (json.dumps(all_data),))
            conn.commit()

            print(self.num_tweets)
            print((username, tweet))

            return True
        else:
            return False


myStreamListener = MyStreamListener()

myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

# Can add multiple tracks
myStream.filter(track=['election2020'], is_async=True)
