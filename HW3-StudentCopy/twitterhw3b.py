# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

import tweepy
from tweepy import OAuthHandler
from tweepy import API 
from tweepy import Cursor
from textblob import TextBlob 

consumer_key = "I1NE9EwNVekvFYkeiiwaoT3iZ"
consumer_secret = "injoKb5LWmAekKH9ALdscuG9B00Gs456kKi3Ykt2uwD3OD5QVM"
access_token = "250423934-mYtCr5i8RHFAN6bXl3sM9QxzgvNeqyazq19BlTbq"
access_secret = "J7rhELXeHkPQ6xDfMtqtxqrctiCmzCO8ZimcZrHnQ7ZDU"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

search_term = input('Input a term: ')
for tweets in tweepy.Cursor(api.search, q=search_term, result_type='recent', include_entities=True, lang='en', count=100).items(100): 
	print (tweets.text)

analysis = TextBlob(tweets.text)
print (analysis.sentiment)

sub = analysis.sentiment.subjectivity
pol = analysis.sentiment.polarity
print ('The average subjectivity is:', sub)
print ('The average polarity is:', pol)

