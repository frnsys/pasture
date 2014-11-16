from sklearn.feature_extraction.text import TfidfVectorizer

def train_model(docs):
    # For tweets, highest max_df (1.0) and lowest min_def (0.0) work best.
    m = TfidfVectorizer(input='content', stop_words=None, lowercase=True, max_df=1.0, min_df=0.0, use_idf=True, smooth_idf=True)
    m.fit(docs)
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
    return s.polarity, s.subjectivity


import numpy as np
from scipy.spatial.distance import cdist

def similar(in_vecs, vecs, threshold=1.1):
    """
    Returns the indices of all distances below the specified threshold.
    Each row in the returned array is the indices for the corresponding row in in_vecs.
    """
    sim_mat = cdist(in_vec.todense(), vecs.todense())
    most_sim = np.where(np.any(sim_mat<threshold), axis=0)
    return most_sim

def most_similar(in_vecs, vecs, n=5):
    """
    Returns the top n most similar indices.
    Each row in the returned array is the indices for the corresponding row in in_vecs.
    """
    sim_mat = cdist(in_vecs.todense(), vecs.todense())
    return np.argsort(y)[:n]

def dissimilar(in_vecs, vecs, threshold=1.1):
    sim_mat = cdist(in_vec.todense(), vecs.todense())
    most_sim = np.where(np.any(sim_mat>threshold), axis=0)
    return most_sim

def least_similar(in_vecs, vecs, n=5):
    sim_mat = cdist(in_vecs.todense(), vecs.todense())
    return np.fliplr(np.argsort(y))[:n]
