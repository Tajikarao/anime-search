from algos.soundex import sndx
from utils.blueprint import Blueprint
from utils.cache import cache
from utils.media import anime

blueprint = Blueprint("soundex")


@blueprint.route("/soundex/<search>/<limit>", methods=["GET"])
@cache.cached(timeout=20)
def soundex(search, limit):
    anime_list = anime.get_names()

    return sndx(anime_list, search, limit)
