import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors


def k_nearest_neighbors(anime_list, search, limit):
    if not limit.isnumeric():
        limit = 10
    limit = int(limit)

    texts = []
    labels = []
    for anime_dict in anime_list:
        for anime_name, variations in anime_dict.items():
            for variation in variations:
                texts.append(variation)
                labels.append(anime_name)

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)

    nbrs = NearestNeighbors(n_neighbors=10, algorithm="auto").fit(X)

    test_text_vector = vectorizer.transform([search])
    distances, indices = nbrs.kneighbors(test_text_vector)

    anime_distances = {}
    for i, index in enumerate(indices[0]):
        label = labels[index]
        distance = distances[0][i]
        if (
            label in anime_distances
            and distance < anime_distances[label]
            or label not in anime_distances
        ):
            anime_distances[label] = distance

    sorted_anime_distances = sorted(anime_distances.items(), key=lambda x: x[1])
    return [anime_name for anime_name, _ in sorted_anime_distances[:limit]]
