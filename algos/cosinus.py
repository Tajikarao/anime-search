import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_distances


def cos(anime_list, search, limit):
    if not limit.isnumeric():
        limit = 10
    limit = int(limit)

    vectorizer = TfidfVectorizer(
        analyzer="char", ngram_range=(1, 3), min_df=0, lowercase=False
    )
    tfidf = vectorizer.fit_transform(anime_list)

    query_vec = vectorizer.transform([search])
    distances = cosine_distances(query_vec, tfidf)

    indices = np.argsort(distances)[0][:limit]
    return [anime_list[i] for i in indices]
