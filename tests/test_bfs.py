from pygraphblas import Matrix, types

from src.bfs import bfs


def test_bfs_1():
    I = [0, 1, 2]
    J = [1, 2, 3]
    V = [True] * len(I)
    G = Matrix.from_lists(I, J, V, 4, 4)
    reachable = bfs(G, [0])
    assert reachable[0][0] == [0]
    assert reachable[0][1] == [0, 1]
    assert reachable[0][2] == [0, 1, 2]
    assert reachable[0][3] == [0, 1, 2, 3]


def test_bfs_2():
    I = [0, 1, 2]
    J = [1, 2, 3]
    V = [True] * len(I)
    G = Matrix.from_lists(I, J, V, 4, 4)
    reachable = bfs(G, [0, 1])
    assert reachable[0][0] == [0]
    assert reachable[0][1] == [0, 1]
    assert reachable[0][2] == [0, 1, 2]
    assert reachable[0][3] == [0, 1, 2, 3]
    assert reachable[1][0] == [1]
    assert reachable[1][1] == [1, 2]
    assert reachable[1][2] == [1, 2, 3]
    assert reachable[1][3] == [1, 2, 3]


def test_bfs_3():
    I = [0, 1, 1, 0, 3, 6, 6, 6, 4, 3, 5, 2]
    J = [1, 6, 4, 3, 0, 3, 4, 2, 5, 2, 2, 5]
    V = [True] * len(I)
    G = Matrix.from_lists(I, J, V, 7, 7)
    reachable = bfs(G, [0, 5, 6])
    assert reachable[0][0] == [0]
    assert reachable[0][1] == [0, 1, 3]
    assert reachable[0][2] == [0, 1, 2, 3, 4, 6]
    assert reachable[0][3] == [0, 1, 2, 3, 4, 5, 6]
    assert reachable[0][4] == [0, 1, 2, 3, 4, 5, 6]
    assert reachable[0][5] == [0, 1, 2, 3, 4, 5, 6]
    assert reachable[0][6] == [0, 1, 2, 3, 4, 5, 6]

    assert reachable[1][0] == [5]
    assert reachable[1][1] == [2, 5]
    assert reachable[1][2] == [2, 5]
    assert reachable[1][3] == [2, 5]
    assert reachable[1][4] == [2, 5]
    assert reachable[1][5] == [2, 5]
    assert reachable[1][6] == [2, 5]

    assert reachable[2][0] == [6]
    assert reachable[2][1] == [2, 3, 4, 6]
    assert reachable[2][2] == [0, 2, 3, 4, 5, 6]
    assert reachable[2][3] == [0, 1, 2, 3, 4, 5, 6]
    assert reachable[2][4] == [0, 1, 2, 3, 4, 5, 6]
    assert reachable[2][5] == [0, 1, 2, 3, 4, 5, 6]
    assert reachable[2][6] == [0, 1, 2, 3, 4, 5, 6]


def test_bfs_isolated_vertices():
    G = Matrix.from_lists([], [], [], 2, 2, typ=types.BOOL)
    reachable = bfs(G, [0, 1])
    assert reachable[0][0] == [0]
    assert reachable[0][1] == [0]
    assert reachable[1][0] == [1]
    assert reachable[1][1] == [1]
