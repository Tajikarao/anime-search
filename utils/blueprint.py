from flask import Blueprint as Flask_Blueprint


class Blueprint:
    def __new__(cls, blueprint: str) -> Flask_Blueprint:
        return Flask_Blueprint(
            blueprint,
            __name__,
        )
