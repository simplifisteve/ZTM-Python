import tweepy
import time

auth = tweepy.OAuth1UserHandler('consumer_key', 'consumer_secret')
auth.set_access_token('access_token', 'access_token_secret')

api = tweepy.API(auth)
user = api.get_user(screen_name='username')


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.TooManyRequests:
        time.sleep(300)


# Generous Follower Bot
for follower in limit_handler(tweepy.Cursor(api.get_followers).items()):
    if follower.name == 'example':  # or set follower.count > 1000 etc
        follower.follow()
        break

# Retweet Bot
for tweet in tweepy.Cursor(api.home_timeline).items():
    try:
        tweet.retweet()
        print('Retweeted the tweet')
        time.sleep(300)
    except tweepy.TweepyException as e:
        print(e)
    time.sleep(5*60)

# Favorite a tweet based on conditions
search_string = 'python'
numberOfTweets = 5

for tweet in tweepy.Cursor(api.search_tweets, q=search_string).items(numberOfTweets):
    try:
        tweet.favorite()
        print('I like that tweet')
    except tweepy.TweepyException as e:
        print(e)
    except StopIteration:
        break
