# bot.py

import tweepy
from secrets import *

# create a class inherithing from the tweepy StreamListener
class BotStreamer(tweepy.StreamListener):

    # Called when a new status arrives which is passed down from the on_data method of the StreamListener
    def on_status(self, status):
        username = status.user.screen_name
        status_id = status.id

    #entities provide structured data from Tweets including resolved URLs, media, hashtags
    #and mentions without having to parse the text to extract that information
        if 'media' in status.entities:
            for image in status.entities['media']:
                tweet_image(image['media_url'], username, status_id)

#create an OAuthHandler instance
#Twitter requires all requests to use OAuth

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

#construts the API instance

api = tweepy.API(auth) #creates API object

#constructs the Stream instance
myStreamListener = BotStreamer()

stream = tweepy.Stream(auth, myStreamListener)
# filter all tweets tweeted at the bot
stream.filter(track=['@capstonebot'])


#reads tweets in timeline

public_tweets = api.user_timeline('Lin_Manuel')
for tweet in public_tweets:
    tweet.text = tweet.text.encode('utf-8')
    print(tweet.text)
