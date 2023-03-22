from algos.soundex_cosine import sndx
from utils.blueprint import Blueprint
from utils.cache import cache
from utils.media import anime

blueprint = Blueprint("soundex_cosine")


@blueprint.route("/soundex_cosine/<search>/<limit>", methods=["GET"])
@cache.cached(timeout=20)
def soundex_cosine(search, limit):
    anime_list = anime.get_names_and_synonyms()

    return sndx(anime_list, search, limit)
