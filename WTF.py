import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'EWj2VMMf0jCrYA1QqhiwuDJqt'
consumer_secret= 'BrbPHXx3yvSCYiA3ZAIWaip9t9JwN7wRAXnGvg1Q7YsJy795HI'

access_token='740938180849897473-ABwa0pf6ZY9oCJyFr0bInlRtqDAECA4'
access_token_secret='VaH5BNFIBK3B0ilKoLoEFPtfs41WXzWNVd1n3FgdL0d8e'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('What the fuck')



#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself


for tweet in public_tweets:
    print(tweet.text)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
