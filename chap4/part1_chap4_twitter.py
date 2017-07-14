from twitter import *

t = Twitter(aouth=OAuth('Access Token','Access Token Secret','Consumer Key','Consumer Secret'))
pythonTweets = t.search.tweets(q = "#python")
print(pythonTweets)
