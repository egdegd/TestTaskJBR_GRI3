from pygraphblas import gviz, Matrix, types


def parse_edge(e, n):
    vertexes = e.split()
    if len(vertexes) != 2:
        raise Exception('Bad format for edge: ' + e)
    a, b = int(vertexes[0]), int(vertexes[1])
    if a >= n:
        raise Exception('Vertices must be less than the number of vertices, but ' + str(a) + ' >= ' + str(n))
    if b >= n:
        raise Exception('Vertices must be less than the number of vertices, but ' + str(b) + ' >= ' + str(n))
    return a, b


def read_graph_from_file(input_file):
    file = open(input_file, 'r')
    lines = file.readlines()
    try:
        n = int(lines[0])
    except:
        raise Exception('Bad format for the number of vertices: ' + lines[0])
    edges = list(map(lambda l: parse_edge(l, n), lines[1:]))
    I = [a for (a, b) in edges]
    J = [b for (a, b) in edges]
    V = [True] * len(I)
    return Matrix.from_lists(I, J, V, n, n, typ=types.BOOL)


def draw_graph_in_file(G, output_file):
    gviz.draw_graph(G, filename=output_file, show_weight=False)
