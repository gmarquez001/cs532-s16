#Obtained from Kevin Clemons
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import time
import json
access_token = "4869609627-lGa4bpRa9bUphIiMvDahxf5L5jT3V83XV5Y1nk6"
access_token_secret = "WKXEjDDhpXxoymBitm6EJdYpCxDFRg7B8Nhg2oewPIIcx"
consumer_key = "U5ALJzwPJF07GjvVvBSnlPlhZ"
consumer_secret = "wmQbiKczoDB3gq7P5OQIu2iaRr89BTIJ4R7tOsfHRjS2AtowgQ"





class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
	ids = []
	tList = {}

	if(api.verify_credentials):
		print("Successfully Logged in")
		print("Getting twitter follower list")
		user = tweepy.Cursor(api.followers,screen_name="phonedude_mln").items()
		while True:
			try:
				u = next(user)
				tList[u.screen_name] = {'number_of_followers':0}
			except:
				print("We got a timeout...sleeping for 15 minutes")
				with open('twitter_followers.json','w') as f:
					json.dump(tList,f)
				time.sleep(15*60)
				

				
				u = next(user)
				tList[u.screen_name] = {'number_of_followers':0}

		with open('twitter_followers.json','w') as f:
			json.dump(tList,f)

	v = open('twitter_followers.json','r')
	tList = json.loads(v.readline())
	for key in tList.keys():
		print(key)
	
	follower_dict = {}

	
	v = 2
