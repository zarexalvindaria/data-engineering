"""Provide a simple data catalog to act as
the single point of truth for the location of
data.

This catalog assumes the data lake is filesystem based.
In realistic situations, it does not have to be.

TODO: improve by making an abstraction of the
 type of the data (database, file: csv/parquet/…, …)
"""

from .config import DATA_LAKE


def _resource(zone, key):
    return str(DATA_LAKE / zone / key)


catalog = {
    "clean/demographics": _resource("clean", "demographics"),
    "business/chinese_demographics": _resource("business",
                                               "chinese_demographics")
}
