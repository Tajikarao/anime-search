from algos.soundex_levenshtein import sndx
from utils.blueprint import Blueprint
from utils.cache import cache
from utils.media import anime

blueprint = Blueprint("soundex_levenshtein")


@blueprint.route("/soundex_levenshtein/<search>/<limit>", methods=["GET"])
@cache.cached(timeout=20)
def soundex_levenshtein(search, limit):
    anime_list = anime.get_names_and_synonyms()

    return sndx(anime_list, search, limit)
