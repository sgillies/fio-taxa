fio_taxa
========

.. image:: https://travis-ci.org/sgillies/fio-taxa.svg
   :target: https://travis-ci.org/sgillies/fio-taxa

.. image:: https://coveralls.io/repos/github/sgillies/fio-taxa/badge.svg?branch=master
   :target: https://coveralls.io/github/sgillies/fio-taxa?branch=master


fio_taxa classifies GeoJSON features.

Given a sequence of Features, fio_taxa finds and returns the set of unique
kinds of Features in the sequence. Uniqueness is determined by geometry type
and by the set of names and types of values in a Feature's 'properties' member.
Members foreign to the GeoJSON specification are not considered.

Usage
-----

fio_taxa has one function: ``fio_taxa.classify()``.

.. code-block:: python

    >>> import json
    >>> from fio_taxa import classify
    >>> src = open('tests/data/trio.geojson')
    >>> collection = json.loads(src.read())
    >>> for taxon in classify(collection['features']):
    ...     print(taxon)
    ...
    ((('aqueduct', 'str'),), 'LineString')
    ((('architect', 'str'), ('name', 'str')), 'Polygon')
    ((('name', 'str'),), 'Point')

Command line interface
----------------------

fio_taxa adds a "taxa" command to Fiona's "fio" program.

.. code-block:: console

    $ cat tests/data/trio.seq | fio taxa
    {"geometry": "Polygon", "properties": {"architect": "str", "name": "str"}}
    {"geometry": "Point", "properties": {"name": "str"}}
    {"geometry": "LineString", "properties": {"aqueduct": "str"}}
