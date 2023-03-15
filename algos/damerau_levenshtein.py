import numpy as np
from jellyfish import damerau_levenshtein_distance


def damerau_lvst(anime_list, search, limit):
    if not limit.isnumeric():
        limit = 10
    limit = int(limit)

    scores = [
        damerau_levenshtein_distance(search.lower(), anime.lower())
        for anime in anime_list
    ]
    indices = np.argsort(scores)[:limit]
    return [anime_list[i] for i in indices]
