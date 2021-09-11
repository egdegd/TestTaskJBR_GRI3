import tempfile
from os import path

from src.graph_processing import read_graph_from_file, parse_edge


def test_read_graph():
    test_dir = tempfile.gettempdir()
    f = open(path.join(test_dir, 'input.txt'), 'w')
    f.write('4\n 0 1\n 1 2\n 2 3\n')
    f.close()
    G = read_graph_from_file(path.join(test_dir, 'input.txt'))
    assert G.to_lists() == [[0, 1, 2], [1, 2, 3], [True, True, True]]


def test_read_empty_graph():
    test_dir = tempfile.gettempdir()
    f = open(path.join(test_dir, 'input.txt'), 'w')
    f.write('1\n')
    f.close()
    G = read_graph_from_file(path.join(test_dir, 'input.txt'))
    assert G.to_lists() == [[], [], []]


def test_parse_edge():
    assert parse_edge('1 2', 3) == (1, 2)
    assert parse_edge('0 0', 3) == (0, 0)
    assert parse_edge('2 1', 3) == (2, 1)
