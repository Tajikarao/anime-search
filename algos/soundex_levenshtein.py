import Levenshtein
from soundex import Soundex


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

    test_text_soundex = soundex.soundex(search)

    anime_distances = {}
    for i, label in enumerate(labels):
        distance = Levenshtein.distance(test_text_soundex, texts[i])
        if (
            label in anime_distances
            and distance < anime_distances[label]
            or label not in anime_distances
        ):
            anime_distances[label] = distance

    sorted_anime_distances = sorted(anime_distances.items(), key=lambda x: x[1])
    return [anime_name for anime_name, _ in sorted_anime_distances[:limit]]