from sklearn.feature_extraction.text import CountVectorizer
from soundex import Soundex
from sklearn.metrics.pairwise import cosine_distances


def sndx(anime_list, search, limit):
    if not limit.isnumeric():
        limit = 10
    limit = int(limit)

    texts = []
    labels = []
    soundex = Soundex()

    for anime_dict in anime_list:
        for anime_name, variations in anime_dict.items():
            for variation in variations:
                texts.append(soundex.soundex(variation))
                labels.append(anime_name)

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(texts)

    test_text_vector = vectorizer.transform([soundex.soundex(search)])
    distances = cosine_distances(test_text_vector, X)

    anime_distances = {}
    for i, label in enumerate(labels):
        distance = distances[0][i]
        if (
            label in anime_distances
            and distance < anime_distances[label]
            or label not in anime_distances
        ):
            anime_distances[label] = distance

    sorted_anime_distances = sorted(anime_distances.items(), key=lambda x: x[1])
    return [anime_name for anime_name, _ in sorted_anime_distances[:limit]]