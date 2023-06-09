from algos.damerau_levenshtein import damerau_lvst
from utils.blueprint import Blueprint
from utils.cache import cache
from utils.media import anime

blueprint = Blueprint("damerau_levenshtein")


@blueprint.route("/damerau_levenshtein/<search>/<limit>", methods=["GET"])
@cache.cached(timeout=20)
def damerau_levenshtein(search, limit):
    anime_list = anime.get_names_and_synonyms()

    return damerau_lvst(anime_list, search, limit)
