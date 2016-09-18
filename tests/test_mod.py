import json

from fio_taxa import classify


def test_taxa():
    with open('tests/data/trio.geojson') as src:
        collection = json.loads(src.read())
        taxa = classify(collection['features'])
        assert len(taxa) == 3
