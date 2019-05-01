# MyTweetBot
Practice Twitter Bot in python

This was done for my capstone project at Cornell College.

## Objective

Create a simple Twitter Bot that would be able to do simple things such as generate replys to people that tweeted it, to generating a random word of the day.

### What is necessary to run the code?

1. You will need API access keys to these three websites.
  * [Twitter](https://developer.twitter.com/content/developer-twitter/en.html)
  * [Wordnik Dictionary](https://developer.wordnik.com/)
  * [OpenWeatherMap](https://openweathermap.org/api)
  
2. A Twitter Account


### What are the commands for the Twitter Bot?

#### !word

This generates a random word for the bot to tweet from the Wordnik API. It also gets the definition and replys to whoever tweeted the account

#### !define (word)

This get the definition to whichever word was tweeted at the bot.

#### !weather (city)

This gets the weather of the selected city in Kelvin and replys to whoever tweeted the bot. Uses the OpenWeatherMap API

#### !image

Scrambles whatever image was sent to the bot and replys with the scrambles image

### What do the other files do?

#### timeline.py

Prints out the last ten tweets on the bot's timeline into terminal

#### wordOfDay.py

Finds a random word and gets the definition and an example case for the word. It is then tweeted out by the bot.

#### retweet.py

Retweets the first five tweets on the bot's timeline. Then the bot tweets out it's own original tweet.

### Future Goals with this project?

I would hopefully get the weather API to give the temperature in fahrenheit or Celcius instead of Kelvin

I would also hope to figure out how to make the bot only take the first word that comes after !weather or !word. Right now if that happens, it just breaks.

I would try to figure out more about pydocs. Right now, it doesn't seem super useful to me, but maybe I could have found more about how to use it correctly with more time

Finally, earlier in the project I tried to have the API generate lyrics with the Genius API but the python support for the API was not working. With more time, I would love to go back and try to make it work.

### Credit to tutorials

https://medium.freecodecamp.org/creating-a-twitter-bot-in-python-with-tweepy-ac524157a607
https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/

