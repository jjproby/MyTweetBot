# reply.py

import tweepy
from secrets import *
import requests

def reply(username, status_id):
	api.update_status("Thank you for tweeting at me, @" + username + "! <3", in_reply_to_status_id = status_id)
	print("reply sent")


class BotStreamer (tweepy.StreamListener):

	def on_status(self, status):
		username = status.user.screen_name
		status_id = status.id
		print(status.text)
		reply(username, status_id)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

#construts the API instance

api = tweepy.API(auth) #creates API object

myStreamListener = BotStreamer()

stream = tweepy.Stream(auth, myStreamListener)

stream.filter(track=['@jjproby719'])
