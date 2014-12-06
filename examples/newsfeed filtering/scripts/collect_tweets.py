"""
Collect tweets via search queries.
You can run this periodically and it will update the data file.
"""

import os
import json
import tweepy

TWITTER_CONSUMER_KEY    = 'fill me in'
TWITTER_CONSUMER_SECRET = 'fill me in'

def _api():
    """
    Setup things on Twitter's end at:
    https://apps.twitter.com/
    """
    auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
    return tweepy.API(auth)

api = _api()

data = []
if os.path.exists('gamergate.json'):
    with open('gamergate.json', 'r') as f:
        data = json.load(f)

tweets = api.search('#gamergate', count=100, result_type='popular')
tweets += api.search('#notyourshield', count=100, result_type='popular')
tweets += api.search('#GamersAgainstGamerGate', count=100, result_type='popular')
tweets += api.search('#stopgamergate2014', count=100, result_type='popular')
tweets += api.search('#opskynet', count=100, result_type='popular')
tweets += api.search('gamergate', count=100, result_type='popular')
tweets += api.search('#antigamergate', count=100, result_type='popular')
tweets += api.search('#notyourscapegoat', count=100, result_type='popular')
tweets += api.search('#shirtgate', count=100, result_type='popular')
tweets += api.search('#freeroguestar', count=100, result_type='popular')
tweets += api.search('roguestar', count=100, result_type='popular')
tweets += api.search('#opmute', count=100, result_type='popular')
tweets += api.search('#femfreq', count=100, result_type='popular')
tweets += api.search('#kotakuinaction', count=100, result_type='popular')

for tweet in tweets:
    data.append({
        'id': tweet.id,
        'favorite_count': tweet.favorite_count,
        'retweet_count': tweet.retweet_count,
        'text': tweet.text,
        'created_at': str(tweet.created_at),
        'user': tweet.user.screen_name,
        'user_created_at': str(tweet.user.created_at),
        'user_tweet_count': tweet.user.statuses_count,
        'user_following_count': tweet.user.friends_count,
        'user_follower_count': tweet.user.followers_count
    })


# Clean up duplicates.
deduped = []
for t in data:
    if t not in deduped and t['text'] not in texts:
        deduped.append(t)

with open('gamergate.json', 'w') as f:
    json.dump(existing_data + data, f, sort_keys=True, indent=4, separators=(',', ': '), encoding='utf-8')
