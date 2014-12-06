import json

# Load up the script's filtered tweets.
# Using the file system like this is kind of slow...
def load_tweets(outpath):
    with open(outpath, 'r') as f:
        tweets = json.load(f)
    return tweets

def build_outpath(id):
    return '/tmp/{0}_out'.format(id)
