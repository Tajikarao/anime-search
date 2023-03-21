from datetime import datetime, timezone

import requests

from utils.singleton import Singleton


class Anime(object, metaclass=Singleton):
    def __init__(self) -> None:
        self.offline_database_anime = {}
        self.last_update_offline_database_anime = False

    def get_offline_database(self):
        current_timestamp = int(datetime.now(tz=timezone.utc).timestamp())

        if (
            not self.last_update_offline_database_anime
            or current_timestamp - 86400 > self.last_update_offline_database_anime
        ):
            self.offline_database_anime = requests.get(
                "https://raw.githubusercontent.com/manami-project/anime-offline-database/master/anime-offline-database.json"
            ).json()

            self.last_update_offline_database_anime = current_timestamp

        return self.offline_database_anime

    def get_names(self):
        database = self.get_offline_database()
        medias = []

        if "data" in database:
            for anime in database["data"]:
                if "Title to be Announced" not in anime["title"]:
                    medias.append(anime["title"])

        return list(set(medias))
    
    def get_names_and_synonyms(self):
        database = self.get_offline_database()
    
        medias = []

        if "data" in database:
            for anime in database["data"]:
                if "Title to be Announced" not in anime["title"]:

                    anime_dict = {}
                    synonyms = []
                    if "synonyms" in anime:
                        synonyms = list(anime["synonyms"])

                    anime_dict[anime["title"]] = synonyms

                    medias.append(anime_dict)

        return medias


anime = Anime()
