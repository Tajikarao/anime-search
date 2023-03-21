from algos.manhattan import mtt
from utils.blueprint import Blueprint
from utils.cache import cache
from utils.media import anime

blueprint = Blueprint("manhattan")


@blueprint.route("/manhattan/<search>/<limit>", methods=["GET"])
@cache.cached(timeout=20)
def manhattan(search, limit):
    anime_list = anime.get_names_and_synonyms()

    return mtt(anime_list, search, limit)
