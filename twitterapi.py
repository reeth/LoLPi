
CONSUMER_KEY = 'INSERT CONSUMER KEY HERE'
CONSUMER_SECRET = 'INSERT CONSUMER SECRET HERE'
ACCESS_KEY = 'INSERT ACCESS KEY HERE'
ACCESS_SECRET = 'INSERT ACESS SECRET HERE' 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
