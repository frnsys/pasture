import sys
import json

# So we can import tools from the app.
# I'd like to find a better way eventually.
sys.path.append('$toolspath')
import tools

# A print method that handles encoding.
def p(x):
    if type(x) is unicode:
        print(x.encode('utf-8'))
    else:
        print(x)

with open('$datapath', 'r') as f:
    TWEETS = json.load(f)


# Returns tweets matching a list of indices.
def tweets_by_indices(indices):
    for idx in indices:
        yield TWEETS[idx]



# Default filtering method.
# This will be overrided.
def filter(tweets):
    return TWEETS[:20]


HELP = """
- HELP ------------------------------
Each tweet has the following data:

id
favorite_count
retweet_count
text
created_at
user
user_created_at
user_tweet_count
user_following_count
user_follower_count


To change what tweets you see in your feed,
define a `filter(tweets)` method which
returns tweet dicts.
- END -------------------------------
"""

# THE USER SCRIPT
$script
# ===============


# This is kind of complex, maybe unnecessarily so, so later I hope to revise it.
# Filter the tweets according to the method,
# then output to a file.
filtered = filter(TWEETS)
with open('$outpath', 'w') as f:
    if filtered is None:
        filtered = []
    json.dump(filtered, f, encoding='utf-8')
