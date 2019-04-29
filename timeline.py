#timeline.py

import tweepy
from secrets import *

'''
@author: Jordan Proby
'''

def getTimeline():
	'''Gets the last ten tweets from the users timeline'''
	public_tweets = api.home_timeline() #prints out the ten recent tweets on timeline
	for tweet in public_tweets:
		print(tweet.text)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth) #opens API instance

getTimeline()
