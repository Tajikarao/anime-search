from algos.jaro_winkler import jaro
from utils.blueprint import Blueprint
from utils.cache import cache
from utils.media import anime

blueprint = Blueprint("jaro_winkler")


@blueprint.route("/jaro_winkler/<search>/<limit>", methods=["GET"])
@cache.cached(timeout=20)
def jaro_winkler(search, limit):
    anime_list = anime.get_names_and_synonyms()

    return jaro(anime_list, search, limit)
