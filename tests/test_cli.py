from click.testing import CliRunner

from fiona.fio.main import main_group


def test_cli_count():
    with open('tests/data/trio.seq') as seq:
        data = seq.read()
    runner = CliRunner()
    result = runner.invoke(main_group, ['taxa'], input=data)
    assert result.exit_code == 0
    assert '{"properties": {"aqueduct": "str"}, "geometry": "LineString"}' in result.output
    assert '{"properties": {"architect": "str", "name": "str"}, "geometry": "Polygon"}' in result.output
    assert '{"properties": {"name": "str"}, "geometry": "Point"}' in result.output
