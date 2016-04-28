#! /usr/bin/env python
import tweepy
from tweepy import OAuthHandler
import clean_words

ckey = ''
csecret = ''
atoken = ''
asecret = ''

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)

def get_tweet(tweet_number, ScreenName):
    tweetList=[]
    for tweet in tweepy.Cursor(api.search, q=ScreenName, lang="en").items(tweet_number):
        tweetList.append(tweet.text)
    return clean_words.cleanup(tweetList)

