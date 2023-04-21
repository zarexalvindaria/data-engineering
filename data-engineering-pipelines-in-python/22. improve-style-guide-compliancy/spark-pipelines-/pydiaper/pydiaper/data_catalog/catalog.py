from ..config import DATA_LAKE


def _resource(zone, key):
    return str(DATA_LAKE / zone / key)


catalog = {
    "clean/prices": _resource("clean", "prices"),
    "clean/ratings": _resource("clean", "ratings"),
    "landing/ratings": _resource("landing", "ratings.csv"),
    "landing/prices": _resource("landing", "prices.csv"),
}
