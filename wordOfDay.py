#wordOfDay.py

from wordnik import *
from secrets import *
import tweepy


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

tweetApi = tweepy.API(auth)

wordClient = swagger.ApiClient(apiKey, apiUrl)

wordApi = WordApi.WordApi(wordClient)

"""
example = wordApi.getWord('irony')
print example.word
"""


randomApi = WordsApi.WordsApi(wordClient)
random = randomApi.getRandomWord()
print random.word.capitalize()

randomlist = wordApi.getDefinitions(random.word)
print randomlist[0].text


tweetApi.update_status("Random word for everyone! \n" + random.word.capitalize() + ": " + randomlist[0].text)

print("Tweet sent!")
