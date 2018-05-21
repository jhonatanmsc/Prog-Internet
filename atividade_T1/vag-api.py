import requests
import pprint
import json
pp = pprint.PrettyPrinter()

url = 'https://api.vagalume.com.br/search.'

user = requests.get(url+'art?q='+'Coldplay&limit=5')
print('- Get banda -')
pp.pprint(user.json())

mus = requests.get(url+'excerpt?q='+'red&limit=5')
pp.pprint(mus.json())