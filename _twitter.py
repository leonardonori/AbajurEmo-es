# -*- coding: utf-8 -*-
import sys
sys.path.append("dir_path")
from _connection import *
import tweepy
import sys

def getTweets(hashtag, numTweets):

	consumer_key = ''
	consumer_secret = ''
	access_token = ''
	access_secret = ''

	OAUTH_KEYS = {'consumer_key':consumer_key, 'consumer_secret':consumer_secret,
	 'access_token_key':access_token, 'access_token_secret':access_secret}
	auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])
	api = tweepy.API(auth)

	cricTweet = tweepy.Cursor(api.search, q=hashtag).items(numTweets)
	tweets = []
	for tw in cricTweet:
		tmp =  {"id":tw.id,"text":tw.text}
		tmp['text'] = tmp['text'].replace('\n',' ')
		tmp['text'] = tmp['text'].replace('\t',' ')
		tweets.append(tmp)

	return tweets

def insertTweets(array, db):
	cursor = db.cursor()
	for tweet in array:
		query = 'INSERT INTO tweets(id_tweet, tweet) VALUES(%d, "%s")' % (tweet['id'], tweet['text'].encode('unicode_escape'))
		#print (query)+"\n"
		try:
			cursor.execute(query)
		except mysql.connector.Error as err:
			pass

	db.commit()
	cursor.close()


def downloadTweets(hashtag, numTweets):
	db = getConnection()
	cursor = db.cursor()
	tweets = []
	tweets = getTweets(hashtag, numTweets)
	insertTweets(tweets, db)
	db.close();
