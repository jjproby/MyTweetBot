#wordOfDay.py

from wordnik import *
from secrets import *
import tweepy


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

tweetApi = tweepy.API(auth)

wordClient = swagger.ApiClient(apiKey, apiUrl)

wordApi = WordApi.WordApi(wordClient)

randomApi = WordsApi.WordsApi(wordClient) #starts an API client
random = randomApi.getRandomWord() #get the random word from Wordnik
print random.word.capitalize()

randomlist = wordApi.getDefinitions(random.word) #Gets a list of the definitions for the word generated
print randomlist[0].text


wordExample = wordApi.getExamples(random.word)  #Gets a list of examples cases for the word
print wordExample.examples[1].text

wordTweet = "Random word for everyone! \n" + random.word.capitalize() + ": " + randomlist[0].text + "\n" + wordExample.examples[1].text


if wordTweet < 280: #If a tweet is more than 280 characters, tweet the definition and the word without the example.
    tweetApi.update_status(wordTweet)
else:
    tweetApi.update_status("Random word for everyone! \n" + random.word.capitalize() + ": " + randomlist[0].text)


print("Tweet sent!")
