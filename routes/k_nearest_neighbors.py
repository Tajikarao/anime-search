from algos.k_nearest_neighbors import k_nearest_neighbors as knn
from utils.blueprint import Blueprint
from utils.cache import cache
from utils.media import anime

blueprint = Blueprint("k_nearest_neighbors")


@blueprint.route("/k_nearest_neighbors/<search>/<limit>", methods=["GET"])
@cache.cached(timeout=20)
def k_nearest_neighbors(search, limit):
    anime_list = anime.get_names_and_synonyms()

    return knn(anime_list, search, limit)
