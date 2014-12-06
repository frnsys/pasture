"""
Anonymizes data and constructs a social graph out of Twitter data.
"""

# -*- coding: utf-8 -*-

import re
import json
import random
from datetime import datetime

# For visualization.
import matplotlib.pyplot as plt
import networkx as nx
import subprocess as sp
from networkx.readwrite import json_graph

from pasture.names import random_name

# Load data.
print('Loading data...')
with open('app/assets/raw/gamergate.json', 'r') as f:
    tweets = json.load(f)


# Create a social graph.
social_graph = nx.DiGraph()


# First pass:
# Create fake usernames for all users.
print('Generating fake usernames...')
users = {}
tweets_by_users = {}
for tweet in tweets:
    # Generate new ids.
    tweet['id'] = str(hash(datetime.utcnow()))[1:]
    if tweet['user'] not in users:
        rand_name = random_name()
        users[tweet['user']] = rand_name
        tweets_by_users[rand_name] = []
    name = users[tweet['user']]
    tweet['user'] = name
    tweets_by_users[name].append(tweet['text'])
new_users = [new_name.decode('utf-8') for real_name, new_name in users.items()]


# Second pass:
# Cleanup all @mentions.
print('Blacking out mentions...')
mention_re = re.compile(r'@[^\s:]+')
for tweet in tweets:
    for match in mention_re.findall(tweet['text']):
        username = match[1:]

        # If this user A mentions another user A, connect A to B.
        if username in users:
            social_graph.add_edge(tweet['user'].decode('utf-8'), users[username].decode('utf-8'))

        blackout = '@' + (len(username) * u'░')
        tweet['text'] = tweet['text'].replace(match, blackout)


def most_common_hashtag(user):
    # Find tweets of this user and get their most commonly-used hashtag.
    hashtags = []
    for t in tweets_by_users[user]:
        for match in hashtag_re.findall(t):
            hashtags.append(match)
    if hashtags:
        return max(set(hashtags), key=hashtags.count)

def find_matching_node_by_hashtag(hashtag, graph):
    # Randomly select a node where a user also mentions this hashtag.
    attempts = 0
    while attempts <= 20:
        attempts += 1

        n = random.choice(graph.nodes()).encode('utf-8')
        for t in tweets_by_users[n]:
            if hashtag in t:
                return n

# For any user not connected to the graph,
# connect by hashtags.
# This is not very efficient but we're not working with a huge amount of data :\
print('Adding disconnected users to the social graph...')
hashtag_re = re.compile(r'#[^\s]+')
for user in users.values():
    if not social_graph.has_node(user):
        #print('No node found for {0}'.format(user))
        hashtag = most_common_hashtag(user)

        if hashtag is not None:
            node = find_matching_node_by_hashtag(hashtag, social_graph)
            if node is not None:
                social_graph.add_edge(user, node)


# Try and connect disconnected subgraphs.
subgraphs = [sg for sg in nx.weakly_connected_component_subgraphs(social_graph)]
main_graph = subgraphs[0]
for sg in subgraphs[1:]:
    n = random.choice(sg.nodes()).encode('utf-8')
    hashtag = most_common_hashtag(n)
    if hashtag is not None:
        node = find_matching_node_by_hashtag(hashtag, main_graph)
        if node is not None:
            social_graph.add_edge(n, node)

print('The social graph has {0} nodes connected by {1} edges, out of {2} users.'.format(social_graph.number_of_nodes(), social_graph.number_of_edges(), len(users)))

print('Generating image of the social graph. This may take awhile...')
savepath = '/Users/ftseng/Desktop/gamergate.pdf'
nx.write_dot(social_graph,'/tmp/social_graph.dot')
with open(savepath, 'wb') as out:
    sp.call(['dot', '-Tpdf', '/tmp/social_graph.dot'], stdout=out)

json_g = json_graph.node_link_data(social_graph)
with open('app/assets/gamergate_socialgraph.json', 'w') as f:
    json.dump(json_g, f)

with open('app/static/socialgraph.json', 'w') as f:
    json.dump(json_g, f)


# Save the data.
print('Saving data...')
with open('app/assets/gamergate.json', 'w') as f:
    json.dump(tweets, f)