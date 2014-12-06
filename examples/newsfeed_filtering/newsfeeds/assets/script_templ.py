import imp
import json
from networkx.readwrite import json_graph

# So we can import the toolkit.
# I'd like to find a better way eventually.
toolkit = imp.load_source('toolkit', '$toolkit_path')

# A print method that handles encoding.
def print_(x):
    if type(x) is unicode:
        print(x.encode('utf-8'))
    else:
        print(x)

with open('$datapath', 'r') as f:
    TWEETS = json.load(f)

with open('$graphpath', 'r') as f:
    json_g = json.load(f)
    GRAPH  = json_graph.node_link_graph(json_g)


all_texts = [t['text'] for t in TWEETS]
model = toolkit.train_model(all_texts)
all_vecs = model.transform(all_texts)

# Returns tweets matching a list of indices.
def tweets_by_indices(indices):
    return [TWEETS[idx] for idx in indices]

# Returns tweets matching a list of ids.
# Brute search, not efficient, just a quick solution.
def tweets_by_ids(ids):
    ts = []
    for id in ids:
        for t in TWEETS:
            if t['id'] == str(id):
                ts.append(t)
    return ts

# Returns tweets matching a list of ids.
# Brute search, not efficient, just a quick solution.
def tweets_by_ids(ids):
    for id in ids:
        for t in TWEETS:
            if t['id'] == id:
                yield t


# "Follow" a user in the social graph.
def follow(user):
    if user[0] == '@':
        user = user[1:]
    if user in GRAPH.nodes():
        GRAPH.add_edge('ME', user)


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

To "follow" a user, do:
    follow(username)

To get a list of tweets by a list of indices, do:
    tweets_by_indices(indices)

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
