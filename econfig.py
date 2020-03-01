
'''TWITTER API ACCESS INFORMATION'''

consumer_key = "***REMOVED_API_KEY***"
consumer_secret = "***REMOVED_API_SECRET***"

access_token = "***REMOVED_ACCESS_TOKEN***"
access_token_secret = "***REMOVED_ACCESS_TOKEN_SECRET***"

bearer_token = "***REMOVED_BEARER_TOKEN***"

dev_environment_label = "ProjectProduction"

# curl bearer token response:
# $ curl -u ''<API key>:<API secret key>' \
# >   --data 'grant_type=client_credentials' \
# >   'https://api.twitter.com/oauth2/token'
# {"token_type":"bearer","access_token":"***REMOVED_BEARER_TOKEN***"}(base)