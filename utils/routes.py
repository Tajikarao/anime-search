import importlib
from os import scandir


class Routes:
    def __new__(cls, app):
        for item in scandir("routes"):
            if item.is_file() and "routes" not in item.name:
                item_name = item.name.removesuffix(".py")
                locals()[item_name] = importlib.import_module(f"routes.{item_name}")
                app.register_blueprint(getattr(locals()[item_name], "blueprint"))

        return app.url_map
