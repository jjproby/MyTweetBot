#wordOfDay.py

from wordnik import *

apiUrl = 'http://api.wordnik.com/v4'
apiKey = '9b827dd68c55dc3fd010e05126d08aaeedeec622e6ea8ed29'
client = swagger.ApiClient(apiKey, apiUrl)

wordApi = WordApi.WordApi(client)

"""
example = wordApi.getWord('irony')
print example.word
"""


randomApi = WordsApi.WordsApi(client)
random = randomApi.getRandomWord()
print random.word

randomlist = wordApi.getDefinitions(random.word)
print randomlist[0].text
