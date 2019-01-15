# bot.py

import tweepy
from secrets import *

#create an OAuthHandler instance
#Twitter requires all requests to use OAuth

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

#construts the API instance

api = tweepy.API(auth) #creates API object

#reads tweets in timeline


public_tweets = api.user_timeline('Lin_Manuel')
for tweet in public_tweets:
    tweet.text = tweet.text.encode('utf-8')
    print(tweet.text)
