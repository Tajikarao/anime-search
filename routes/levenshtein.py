from algos.levenshtein import lvst
from utils.blueprint import Blueprint
from utils.cache import cache
from utils.media import anime

blueprint = Blueprint("levenshtein")


@blueprint.route("/levenshtein/<search>/<limit>", methods=["GET"])
@cache.cached(timeout=20)
def levenshtein(search, limit):
    anime_list = anime.get_names()

    return lvst(anime_list, search, limit)
