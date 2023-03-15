import jellyfish
import numpy as np


def jaro_winkler(anime_list, search, limit):
    if not limit.isnumeric():
        limit = 10
    limit = int(limit)

    scores = [
        jellyfish.jaro_winkler(search.lower(), anime.lower()) for anime in anime_list
    ]
    indices = np.argsort(scores)[::-1][:limit]
    return [anime_list[i] for i in indices]
