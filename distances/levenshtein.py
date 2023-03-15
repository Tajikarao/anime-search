import Levenshtein
import numpy as np


def lvst(anime_list, search, limit):
    if not limit.isnumeric():
        limit = 10
    limit = int(limit)

    scores = [
        Levenshtein.distance(search.lower(), anime.lower()) for anime in anime_list
    ]
    indices = np.argsort(scores)[:limit]
    return [anime_list[i] for i in indices]
