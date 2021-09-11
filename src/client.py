from bfs import bfs
from graph_processing import read_graph_from_file, draw_graph_in_file


class Client:
    running = True

    def __init__(self):
        self.commands = {
            "bfs": self.bfs,
            "exit": self.exit,
            "draw": self.draw,
            "reachable": self.reachable,
            "load": self.load,
            "help": self.help
        }
        self.reachable_vertexes = None
        self.G = None
        self.match_vertexes = None

    def run(self):
        while self.running:
            cmd = input().split(" ")
            if len(cmd) == 1:
                self.commands[cmd[0]]()
            if len(cmd) == 2:
                self.commands[cmd[0]](cmd[1])
            if len(cmd) == 3:
                self.commands[cmd[0]](cmd[1], cmd[2])
            if len(cmd) == 4:
                self.commands[cmd[0]](cmd[1], cmd[2], cmd[3])

    def load(self, input_file):
        self.G = read_graph_from_file(input_file)

    def bfs(self, start_vertexes):
        start_vertexes = list(map(int, start_vertexes.split('_')))
        self.reachable_vertexes = bfs(self.G, start_vertexes)
        self.match_vertexes = {k: v for v, k in enumerate(start_vertexes)}

    def draw(self, output_file):
        draw_graph_in_file(self.G, output_file)

    def reachable(self, v, step):
        if int(v) not in self.match_vertexes.keys():
            print('Bad vertex')
        else:
            print(self.reachable_vertexes[self.match_vertexes[int(v)]][min(int(step), self.G.ncols - 1)])

    def help(self):
        print('load <input_file> - load graph from input_file')
        print('bfs <start_vertexes> - execute bfs, start_vertexes must be in the format a_b_c')
        print('draw <output_file> - draw graph in output_file')
        print('reachable <v> <step> - return reachable vertices from vertex <v> in step <step>')
        print('exit - finish the program')

    def exit(self):
        self.running = False


def main():
    client = Client()
    client.run()


if __name__ == "__main__":
    main()
