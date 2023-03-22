from algos.chebyshev import cshev
from utils.blueprint import Blueprint
from utils.cache import cache
from utils.media import anime

blueprint = Blueprint("chebyshev")


@blueprint.route("/chebyshev/<search>/<limit>", methods=["GET"])
@cache.cached(timeout=20)
def chebyshev(search, limit):
    anime_list = anime.get_names_and_synonyms()

    return cshev(anime_list, search, limit)
