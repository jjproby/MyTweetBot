#retweet.py

import tweepy
from secrets import *
from random import *

'''
@author: jjproby
'''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

random_tweets = ["Hello, I am bot", "This is a randomly chosen tweet",
		"Hi, how are you today?", "I like Kanye West", "Hamilton is great"]

i = 0
while i < 5:
	print(public_tweets[i].text)
	api.retweet(public_tweets[i].id)
	print("Retweeted!")
	i+= 1
	#retweets the first five tweets on the timeline


tweet_num = randint(0,4) #picks a random tweet from the array and tweets it
api.update_status(random_tweets[tweet_num])
print(random_tweets[tweet_num])
print("tweet sent!")
