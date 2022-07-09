
class Vertex:
    def __init__(self, value, price):
        self.value = value
        self.edges = {}
        self.price = price

    def add_edge(self, value, weight = 0):
        self.edges[value] = weight

    def get_edges(self):
        return list(self.edges.keys())


class Graph:
    def __init__(self, name):
        self.name = name
        self.graph_dict = {}

    def add_vertex(self, value, price):
        vertex = Vertex(value, price)
        self.graph_dict[value] = vertex

    def add_edge(self, from_v, to_v):
        if from_v in self.graph_dict.keys() and to_v in self.graph_dict.keys():
            weight1 = self.graph_dict[to_v].price - self.graph_dict[from_v].price
            self.graph_dict[from_v].add_edge(to_v, weight1)
            weight2 = self.graph_dict[from_v].price - self.graph_dict[to_v].price
            self.graph_dict[to_v].add_edge(from_v, weight2)

    def stringify(self):
        visit = ["callofduty"]
        visited = {}
        while visit:
            cur_v = visit.pop(0)
            visited[cur_v] = True
            print(cur_v)
            next_vs = self.graph_dict[cur_v].get_edges()
            visit += [v for v in next_vs if v not in visited]


action = Graph("action")
arcade = Graph("arcade")
stealth = Graph("stealth")

graphs = [action, arcade, stealth]

action_games = [["Call Of Duty", 34], ["Metal Gear", 22], ["Counter Strike", 0], ["Far Cry", 53], ["Red Dead Redemption", 50], ["Serious Sam", 59]]
arcade_games = [["Celeste", 17], ["Mario", 10], ["Tertris", 5]]
stealth_games = [["Mark Of Ninja", 14], ["Assassins Creed", 37], ["IGI", 8], ["Commandos", 8], ["Desporados", 54]]

games = ["Red Dead Redemption", "Call Of Duty", "Metal Gear",
 "Counter Strike", "Mario", "Assassins Creed",
  "Command and Conquer", "Celeste", "Mark Of Ninja",
   "Desporados", "IGI", "Serious Sam", "Far Cry", "Tetris", "Commandos"]

games_string = ""
for game in games:
    games_string += game + "\n"


def assign_game(graph, games):
    for game in games:
        graph.add_vertex(game[0], game[1])
        for other in graph.graph_dict.keys():
            if game[0] != other:
                graph.add_edge(game[0], other)

assign_game(action, action_games)
assign_game(arcade, arcade_games)
assign_game(stealth, stealth_games)

print(stealth.graph_dict)


