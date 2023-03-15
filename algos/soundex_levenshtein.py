import Levenshtein
import numpy as np
from soundex import Soundex


def sndx(anime_list, search, limit):
    soundex = Soundex()

    if not limit.isnumeric():
        limit = 10
    limit = int(limit)

    anime_codes = [soundex.soundex(anime.lower()) for anime in anime_list]

    search_code = soundex.soundex(search.lower())

    distances = np.array(
        [Levenshtein.distance(search_code, code) for code in anime_codes]
    )

    indices = np.argpartition(distances, limit)[:limit]

    return [anime_list[i] for i in indices]
