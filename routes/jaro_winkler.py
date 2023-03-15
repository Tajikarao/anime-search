from distances.jaro_winkler import jaro_winkler
from utils.blueprint import Blueprint
from utils.cache import cache
from utils.media import anime

blueprint = Blueprint("jarowinkler")


@blueprint.route("/jarowinkler/<search>/<limit>", methods=["GET"])
@cache.cached(timeout=20)
def jarowinkler(search, limit):
    anime_list = anime.get_names()

    return jaro_winkler(anime_list, search, limit)
