# fio_taxa

import logging

from six import text_type


log = logging.getLogger(__name__)

FIELD_TYPES_MAP = {
    int: 'int',
    float: 'float',
    text_type: 'str',
    type(None): 'null'}


def classify(features):
    """Find the unique classes of features.

    Returns
    -------
    set
        A set of unique feature classes
    """
    taxa = set()
    for feat in features:
        properties = {
            k: FIELD_TYPES_MAP[type(v)] for k, v in feat['properties'].items()}
        prop_keys, prop_types = zip(*properties.items())
        geometry = feat['geometry']['type'] if feat['geometry'] else None
        log.debug("Prop_keys: %s, Prop_types: %s, Geometry: %s",
                  prop_keys, prop_types, geometry)
        taxa.add((tuple(sorted(list(zip(prop_keys, prop_types)))), geometry))
    return taxa
