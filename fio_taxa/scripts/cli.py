# Skeleton of a CLI

from collections import OrderedDict
import json

import click
from fiona.fio.helpers import obj_gen

from fio_taxa import classify


@click.command('taxa', short_help='Classifies GeoJSON features')
@click.pass_context
def taxa(ctx):
    """Classifies GeoJSON features.

    Given a sequence of GeoJSON features (RS-delimited or not) on stdin
    this command writes out a JSON description of each unique kind
    (taxon) of feature in the sequence.

    The descriptions have two members: 'properties' and 'geometry'.
    The former is an object describing properties and their types. The
    value of the latter is one of the GeoJSON geometry type names.
    """
    stdin = click.get_text_stream('stdin')
    for taxon in classify(obj_gen(stdin)):
        text = json.dumps(OrderedDict(
            properties=OrderedDict(taxon[0]),
            geometry=taxon[1]))
        click.echo(text)
