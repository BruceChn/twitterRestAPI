import tweepy
import json
from tweepy import OAuthHandler
from flask import jsonify

consumer_key = 'YBD3K3ZM7H5XR8pX2sVQFrr5b'
consumer_secret = '0lXmQN6SJRhrc11b8Z7y27NCGUEhaUFWfRwGcKFUHHd58NUKih'
access_token = '1617281016-ORUfJiXvvTyYT19txrVowD7kCYYS8XLUWXhZeKq'
access_secret = 'utOUeJiwyZKkZJ2xMROuklWO79oa95H9UQX66VHMzLiXE'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
api.wait_on_rate_limit = True
api.retry_count = 5
f = open('tweets1.txt','w')
WORLD_WOE_ID = 1
US_WOE_ID = 23424977
class MyStreamListener(tweepy.StreamListener):

	def on_error(self, status_code):
		if status_code == 420:
            #returning False in on_data disconnects the stream
			return False
	def on_status(self, status):
		f.write(json.dumps(status._json,indent = 1))
		
#def process_or_store(page):
	#for tweet in page:
		#f.write(json.dumps(tweet._json,indent = 1))
	#print(json.dumps(tweet))

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener = MyStreamListener())
myStream.filter(locations = [-122.75,36.8,-121.75,37.8],async = True)

#for page in tweepy.Cursor(api.followers,id = 96054018).pages():
#	process_or_store(page)

#for tweet in tweepy.Cursor(api.friends_timeline).items(200):
	#process_or_store(tweet._json)
	

	
