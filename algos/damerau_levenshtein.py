import numpy as np
from jellyfish import damerau_levenshtein_distance


def damerau_lvst(anime_list, search, limit):
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

    distances = np.array([damerau_levenshtein_distance(search, text) for text in texts])
    indices = np.argsort(distances)

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