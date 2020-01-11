import tweepy
from tweepy import OAuthHandler
import json
import io
import time

#create your own twitter app at https://developer.twitter.com and replace the name at testapp below 
APP_NAME = 'testapp'
 
# Consumer keys and access tokens, used for OAuth
CONSUMER_KEY = 'xxxxxxxxxxxxxxxxxxxxxxx'
CONSUMER_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxx'
ACCESS_TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxx'
ACCESS_TOKEN_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxx'
 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

results = api.trends_place(23424833)	#The Geo ID for Greece 
data = results[0] 
trends = data['trends']
names = [trend['name'] for trend in trends]
trendsNames = ' '.join(names)
f = open('toptrendsdate.txt', 'a')
g = open('toptrends.txt', 'a')
f.write(time.strftime("%d/%m/%Y") + ' ' + trendsNames.encode('utf8') + '\n')  
g.write(trendsNames.encode('utf8') + '\n')
f.close()
g.close()
