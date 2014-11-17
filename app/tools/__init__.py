"""
These are methods which are exposed to the script executed for the user.
Most of these are simplifications or convenience methods.
"""


from sklearn.feature_extraction.text import TfidfVectorizer

def train_model(docs):
    # For tweets, highest max_df (1.0) and lowest min_def (0.0) work best.
    m = TfidfVectorizer(input='content', stop_words=None, lowercase=True, max_df=1.0, min_df=0.0, use_idf=True, smooth_idf=True)
    m.fit(docs)

    # To vectorize, use m.transform(docs)
    return m


from textblob import TextBlob

def sentiment(text):
    """
    Sentiment for a text.

    Polarity: [-1, 1]
    Subjectivity: [0, 1]
    """
    t = TextBlob(text)
    s = t.sentiment
    #return s.polarity, s.subjectivity
    return s.polarity


import numpy as np
from scipy.spatial.distance import cdist, pdist, squareform

def similar(in_vecs, vecs, threshold=1.1, metric='euclidean'):
    """
    Returns the indices of all distances below the specified threshold.
    Each row in the returned array is the indices for the corresponding row in in_vecs.
    """
    sim_mat = cdist(in_vec.todense(), vecs.todense(), metric=metric)
    most_sim = np.where(np.any(sim_mat<threshold), axis=0)
    return most_sim

def most_similar(in_vecs, vecs, n=5, metric='euclidean'):
    """
    Returns the top n most similar indices.
    Each row in the returned array is the indices for the corresponding row in in_vecs.
    """
    sim_mat = cdist(in_vec.todense(), vecs.todense(), metric=metric)
    return np.argsort(sim_mat).flatten()[:n]

def dissimilar(in_vecs, vecs, threshold=1.1, metric='euclidean'):
    sim_mat = cdist(in_vec.todense(), vecs.todense(), metric=metric)
    most_sim = np.where(np.any(sim_mat>threshold), axis=0)
    return most_sim

def least_similar(in_vecs, vecs, n=5, metric='euclidean'):
    sim_mat = cdist(in_vecs.todense(), vecs.todense(), metric=metric)
    return np.fliplr(np.argsort(sim_mat).flatten())[:n]

def most_salient(vecs, n=5, metric='euclidean'):
    """
    The most salient indices, that is, those that are most dissimilar from the bunch.
    """
    sim_mat = squareform(pdist(vecs, metric=metric))
    means = np.mean(sim_mat, axis=1)
    return np.argsort(means)[:n]

def most_representative(vecs, n=5, metric='euclidean'):
    sim_mat = squareform(pdist(vecs, metric=metric))
    means = np.mean(sim_mat, axis=1)
    return np.argsort(means)[::-1][:n]


import networkx as nx

def in_degree_centrality(graph):
    """
    Calculates the (incoming) degree centrality (fraction of nodes a node is connected to)
    for each node in the graph.
    """
    return nx.centrality.in_degree_centrality(graph)

def shortest_path(node_A, node_B, graph):
    """
    Returns the shortest path between two nodes.
    """
    return nx.shortest_paths.shortest_path(graph, node_A, node_B)
