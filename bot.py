# bot.py

'''

@author: jjproby

'''


import tweepy
from secrets import *
from wordnik import *
import requests
from io import BytesIO
from PIL import Image
import random
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

def tweet_image(url, username, status_id):
    filename = 'temp.png'
    #send a get request
    request = requests.get(url, stream = True)
    if request.status_code == 200:
        #read data from downloaded bytes and return a PIL.Image.Image object
        i = Image.open(BytesIO(request.content))
        #Saves the image under the given filename
        i.save(filename)
        scramble(filename)
        #Update the authenticated user's status
        api.update_with_media('scramble.png', status='@{0}'.format(username), in_reply_to_status_id=status_id)
	print("tweet sent!")
    else:
        print("unable to download image")


def scramble(filename):
    BLOCKLEN = 64

    img = Image.open(filename)
    width, height = img.size

    xblock = width // BLOCKLEN
    yblock = height // BLOCKLEN
    # creates sequence of 4-tuples (box) defining the left, upper, right, and lower pixel coordinate
    blockmap = [(xb * BLOCKLEN, yb * BLOCKLEN, (xb + 1) * BLOCKLEN, (yb + 1) * BLOCKLEN)
                for xb in range(xblock) for yb in range(yblock)]

    shuffle = list(blockmap)

    #shuffle the sequence
    random.shuffle(shuffle)

    # Creates a new image with given mode and size
    result = Image.new(img.mode, (width, height))
    for box, sbox in zip(blockmap, shuffle):
        #returns a rectangular region from this original image.
        crop = img.crop(sbox)
        # Pastes the cropped pixel into the new image Object
        result.paste(crop, box)
    result.save('scramble.png')

def reply(username, status_id):
	api.update_status("Thank you for tweeting at me, @" + username + "! <3", in_reply_to_status_id = status_id)
	print("reply sent")

def randomWord(username, status_id):
    randomApi = WordsApi.WordsApi(wordClient)
    random = randomApi.getRandomWord()
    randomlist = wordApi.getDefinitions(random.word)
    api.update_status("@" + username + " \n" + random.word.capitalize() + ": " + randomlist[0].text, in_reply_to_status_id = status_id)
    print("Tweet Sent")

def weather(username, status_id, city_name, api_key):
	  
	# base_url variable to store url 
	base_url = "http://api.openweathermap.org/data/2.5/weather?"
	  
	# complete_url variable to store 
	# complete url address 
	complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
	  
	response = requests.get(complete_url) 
	  
	x = response.json() 
	  
	# Now x contains list of nested dictionaries 
	# Check the value of "cod" key is equal to 
	# "404", means city is found otherwise, 
	# city is not found 
	if x["cod"] != "404": 
	  
	    # store the value of "main" 
	    # key in variable y 
	    y = x["main"] 

	    current_temperature = y["temp"] 

	    current_pressure = y["pressure"] 
	  
	    current_humidiy = y["humidity"] 

	    z = x["weather"] 
	  
	    # store the value corresponding  
	    # to the "description" key at  
	    # the 0th index of z 
	    weather_description = z[0]["description"] 
	    api.update_status("@" + username + " " + city_name + " Weather: " + "\n Temperature (in kelvin unit) = " +
		            str(current_temperature) + 
		  "\n atmospheric pressure (in hPa unit) = " +
		            str(current_pressure) +
		  "\n humidity (in percentage) = " +
		            str(current_humidiy) +
		  "\n description = " +
		            str(weather_description), in_reply_to_status_id = status_id) 
	  
	else: 
	    api.update_status("@" + username + " City Not Found ", in_reply_to_status_id = status_id)
	print("Tweet Sent")

def definition(username, status_id, word):
	wordlist = wordApi.getDefinitions(word)
	api.update_status("@" + username + " \n" + word.capitalize() + ": " + wordlist[0].text, in_reply_to_status_id = status_id)
	print("Tweet Sent")
	


# create a class inherithing from the tweepy StreamListener
class BotStreamer(tweepy.StreamListener):

    # Called when a new status arrives which is passed down from the on_data method of the StreamListener
    def on_status(self, status):
        username = status.user.screen_name
        status_id = status.id
        print("Tweet recieved!")

    #entities provide structured data from Tweets including resolved URLs, media, hashtags
    #and mentions without having to parse the text to extract that information
        if 'media' in status.entities:
		if "!image" in status.text:
			for image in status.entities['media']:
		        	tweet_image(image['media_url'], username, status_id)
		else:
			api.update_status("Thank you for the wonderful photo, @" + username + "! <3", in_reply_to_status_id = status_id)
			print("reply sent") 
			
        elif "!word" in status.text:
            randomWord(username, status_id)
	elif "!weather" in status.text:
		city = status.text[21:]
		print status.text[21:]
		weather(username, status_id, city, weather_api)
	elif "!define" in status.text:
		word = status.text[20:]
		print status.text[20:]
		definition(username, status_id, word)

        else:
            reply(username, status_id)


#create an OAuthHandler instance
#Twitter requires all requests to use OAuth

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

#construts the API instance

api = tweepy.API(auth) #creates API object

wordClient = swagger.ApiClient(apiKey, apiUrl)

wordApi = WordApi.WordApi(wordClient)

#constructs the Stream instance
myStreamListener = BotStreamer()

stream = tweepy.Stream(auth, myStreamListener)
# filter all tweets tweeted at the bot
stream.filter(track=['@jjproby719'])

print("Stream failed")
