#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import requests
import urllib2

#import pandas as pd
#import matplotlib.pyplot as plt

#Acquired from http://adilmoujahid.com/posts/2014/07/twitter-analytics/
#Variables that contains the user credentials to access Twitter API 
access_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_token_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
consumer_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
consumer_secret = "xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

List = []
i = iter(List)
test = open('./testfile.txt' , 'w+')
#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    
    def on_data(self, data):
        if len(List) >= 1000:
            return False
        #Acquired from Matt Payne
        json_code = json.loads(data)
        json_code= json_code['user']

        if json.dumps(json_code['url'], sort_keys = True, indent=4) != "null":
        #Accquired from Matt Payne
        #Gabriel Marquez
            print json.dumps(json_code['url'])
            a = json.dumps(json_code['url'])
            a = a[1:-1]
            # b = None
            b =requests.head("https://www.google.com/")
            try:
                b = requests.head(a)
            except requests.exceptions.ConnectionError:
                b.status_code = "Connection Refused"
            #b = urllib2.urlopen(a)
            #c = b.info().getheader('Status')
            #print c
            if b.status_code == 200 and  a not in List:
                List.append(a)
                test.write(a + '\n')
                print a
                print len(List)
            #for item in List:
            #    print item
            #print len(List)
        return True
        #Gabriel Marquez            

    def on_error(self, status):
        pass


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
#http://adilmoujahid.com/posts/2014/07/twitter-analytics/     
