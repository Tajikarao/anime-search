import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from soundex import Soundex
from sklearn.metrics.pairwise import cosine_distances


def sndx(anime_list, search, limit):
    soundex = Soundex()

    if not limit.isnumeric():
        limit = 10
    limit = int(limit)
    
    soundex_list = [soundex.soundex(anime.lower()) for anime in anime_list]
    search_soundex = soundex.soundex(search.lower())
    soundex_indices = [i for i, soundex_code in enumerate(soundex_list) if soundex_code == search_soundex]
    
    if not soundex_indices:
        return []
    
    vectorizer = TfidfVectorizer(
        analyzer="char", ngram_range=(1, 3), min_df=0, lowercase=False
    )
    tfidf = vectorizer.fit_transform([anime_list[i].lower() for i in soundex_indices])
    
    query_vec = vectorizer.transform([search.lower()])
    distances = cosine_distances(query_vec, tfidf).flatten()
    indices = np.argsort(distances)[:limit]
    return [anime_list[soundex_indices[i]] for i in indices]