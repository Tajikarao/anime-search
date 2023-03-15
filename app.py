from flask import Flask
from flask_talisman import Talisman
from gevent.pywsgi import WSGIServer

from utils.cache import cache
from utils.routes import Routes

flask_config = {
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 300,
}


flask = Flask(__name__)
talisman = Talisman(flask, force_https=False)
cache.init_app(flask, config=flask_config)
routes = Routes(flask)

if __name__ == "__main__":
    WSGIServer(("localhost", 5000), flask).serve_forever()
