import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import manhattan_distances


def mtt(anime_list, search, limit):
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

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(texts)

    test_text_vector = vectorizer.transform([search])

    distances = manhattan_distances(X, test_text_vector)

    indices = np.argsort(distances.ravel())[:limit]

    anime_distances = {}
    for index in indices:
        label = labels[index]
        distance = distances[index]
        if (
            label in anime_distances
            and distance < anime_distances[label]
            or label not in anime_distances
        ):
            anime_distances[label] = distance

    sorted_anime_distances = sorted(anime_distances.items(), key=lambda x: x[1])
    return [anime_name for anime_name, _ in sorted_anime_distances[:limit]]