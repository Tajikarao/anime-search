from algos.cosinus import cos
from utils.blueprint import Blueprint
from utils.cache import cache
from utils.media import anime

blueprint = Blueprint("cosinus")


@blueprint.route("/cosinus/<search>/<limit>", methods=["GET"])
@cache.cached(timeout=20)
def cosinus(search, limit):
    anime_list = anime.get_names()

    return cos(anime_list, search, limit)
