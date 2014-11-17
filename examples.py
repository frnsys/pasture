"""
Some examples.
"""

# Rank by favorite count.
def filter(tweets):
    return sorted(tweets, key=lambda t: t['favorite_count'], reverse=True)

# Filter by favorite count.
def filter(tweets):
    return [t for t in tweets if t['favorite_count'] > 50]

# Rank by retweet count.
def filter(tweets):
    return sorted(tweets, key=lambda t: t['retweet_count'], reverse=True)

# Filter by retweet count.
def filter(tweets):
    return [t for t in tweets if t['retweet_count'] > 50]

# Filter by certain keyword.
def filter(tweets):
    return [t for t in tweets if '#stopgamergate2014' in t['text'].lower()]

# Rank by similarity to favorites.
def filter(tweets):
    fav_ids = [532697698357362688, 532697681081405441, 532697671245381632, 532697669870051328, 532697661862715393]
    favorites = [t for t in tweets_by_ids(fav_ids)]
    fav_vecs = model.transform([t['text'] for t in favorites])

    top_similar_indices = tools.most_similar(fav_vecs, all_vecs, n=20)
    return [t for t in tweets_by_indices(top_similar_indices) if t not in favorites]

# Rank by salience (most dissimilar from all tweets).
def filter(tweets):
    indices = tools.most_salient(all_vecs, n=20)
    return tweets_by_indices(indices)

# Rank by representativeness(most similar to all tweets).
def filter(tweets):
    indices = tools.most_representative(all_vecs, n=20)
    return tweets_by_indices(indices)

# Rank by your degrees of separation (shorter = better).
def filter(tweets):
    # Change this:
    follow('DefiniteKoreanElephant')
    follow('NiceExperimentalPeafowl')

    return sorted(tweets, key=lambda t: tools.shortest_path('ME', t['user'], GRAPH))

# Rank by degrees of separation with people you fav.
# Not implemented.

# Rank by influence (in degree centrality, i.e. num of mentions).
def filter(tweets):
    # TO DO
    print(tools.indegree_centrality(GRAPH))

# Rank by influence (number of followers)
def filter(tweets):
    return sorted(tweets, key=lambda t: t['user_follower_count'], reverse=True)

# Rank by influence (number of followers over following)
def filter(tweets):
    return sorted(tweets, key=lambda t: t['user_follower_count']/t['user_following_count'], reverse=True)

# Rank by smaller voices (less frequent tweets)
def filter(tweets):
    return sorted(tweets, key=lambda t: t['user_tweet_count'])