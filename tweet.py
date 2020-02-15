import twitter
from config import *
import os
import json

api = twitter.Api(consumer_key= consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token_key,
                  access_token_secret=access_token_secret,
                  input_encoding=encoding)

# def main():
#     with open('output.txt', 'a') as f:
#         api.GetStreamFilter will return a generator that yields one status
#         message (i.e., Tweet) at a time as a JSON dictionary.
#         for line in api.GetStreamFilter(track=USERS, languages=LANGUAGES):
#             f.write(json.dumps(line))
#             f.write('\n')


# if __name__ == '__main__':
#     main()

