from pygraphblas import Matrix, Vector


def bfs(G: Matrix, start_vertexes):
    reachable = []
    reachable_vertexes_by_steps = [[] for _ in start_vertexes]
    for v in start_vertexes:
        reachable.append(Vector.from_lists([v], [True], G.ncols))
    for _ in range(G.ncols):
        for i, vector in enumerate(reachable):
            reachable_vertexes_by_steps[i].append(vector.to_lists()[0])
            vector += (vector @ G)
    return reachable_vertexes_by_steps
