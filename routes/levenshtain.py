from distances.levenshtain import lvst
from utils.blueprint import Blueprint
from utils.cache import cache
from utils.media import anime

blueprint = Blueprint("levenshtain")


@blueprint.route("/levenshtain/<search>/<limit>", methods=["GET"])
@cache.cached(timeout=20)
def levenshtain(search, limit):
    anime_list = anime.get_names()

    return lvst(anime_list, search, limit)
