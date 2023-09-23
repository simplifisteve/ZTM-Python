import tweepy
import time

auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
auth.set_access_token('access_token', 'access_token_secret')

api = tweepy.API(auth)
user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)


# Generous Follower Bot
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if follower.name == 'example':  # or set follower.count > 1000 etc
        follower.follow()
        break

# Retweet Bot
for tweet in tweepy.Cursor(api.home_timeline).items():
    try:
        tweet.retweet()
        print('Retweeted the tweet')
        time.sleep(300)
    except tweepy.TweepError as e:
        print(e.reason)
    time.sleep(5*60)

# Favorite a tweet based on conditions
search_string = 'python'
numberOfTweets = 5

for tweet in tweepy.Cursor(api.search, q=search_string).items(numberOfTweets):
    try:
        tweet.favorite()
        print('I like that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
