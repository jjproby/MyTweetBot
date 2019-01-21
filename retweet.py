#retweet.py

import tweepy
from secrets import *
from random import *

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
	

tweet_num = randint(0,4)
api.update_status(random_tweets[tweet_num])
print(random_tweets[tweet_num])
print("tweet sent!")
