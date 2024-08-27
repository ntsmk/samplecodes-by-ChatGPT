import tweepy

# Authenticate to Twitter
# check it developer site
client = tweepy.Client(
    consumer_key='',
    consumer_secret='',
    access_token='',
    access_token_secret=''
)


# Create a tweet
tweet = "and this is just test, you know"
client.create_tweet(text=tweet)
print("Tweeted successfully!")
