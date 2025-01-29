# Finger exercise: Modify the DFS algorithm to find a path that
# minimizes the sum of the weights. Assume that all weights are
# positive integers.

class Node(object):
    def __init__(self, name):
        """Assumes name is a string"""
        self._name = name
    def get_name(self):
        return self._name
    def __str__(self):
        return self._name    


class Edge(object):
    def __init__(self, src, dest):
        """Assumes source and destination are nodes"""
        self._src = src
        self._dest = dest
    def get_source(self):
        return self._src
    def get_destination(self):
        return self._dest
    def __str__(self):
        return self._src.get_name() + '->' + self._dest.get_name()


class Weighted_edge(Edge):
    def __init__(self, src, dest, weight=1):
        super().__init__(src, dest)
        self._weight = weight
    def get_weight(self):
        return self._weight
    def __str__(self):
        return super().__str__() + f'({self._weight})'


class Digraph(object):
    # nodes is a list of nodes in the graph
    # edges is a dict mapping each node to a list of its edges
    def __init__(self):
        self._nodes = []
        self._edges = {}
    def add_node(self, node):
        if node in self._nodes:
            raise ValueError('Duplicate node')
        else:
            self._nodes.append(node)
            self._edges[node] = []
    def add_edge(self, edge):
        src = edge.get_source()
        dst = edge.get_destination()
        if not (src in self._nodes and dst in self._nodes):
            raise ValueError('Node not in graph')
        self._edges[src].append(edge)
    def edges_of(self, node):
        return self._edges[node]
    def has_node(self, node):
        return node in self._nodes
    def __str__(self):
        result = []
        for node in self._nodes:
            for edge in self._edges[node]:
                result.append(str(edge))
        return '\n'.join(result)

class Graph(Digraph):
    def add_edge(self, edge):
        Digraph.add_edge(self, edge)
        rev = Edge(edge.get_destination(), edge.get_source())
        Digraph.add_edge(self, rev)


def print_path(path):
    """Assumes path is a list of edges"""
    result = []
    for e in path:
        result.append(str(e))
    return '[' + ', '.join(result) + ']'
    
def already_visited(node, path):
    for e in path:
        if node == e.get_source():
            return True
    return False

def DFS(graph, start, end, lt, path, shortest, to_print=False):
    """Assumes graph is a Digraph; start and end are nodes;
       lt is a less than function lt(path, shortest);
       path and shortest are lists of edges
       Returns a shortest path from start to end in graph"""
    if to_print:
        print("Current DFS path:", print_path(path))
    if start == end:
        return path
    for e in graph.edges_of(start):
        next = e.get_destination()
        if already_visited(next, path): # avoid cycles
            continue
        new_path = DFS(graph, next, end, lt, path + [e], shortest, to_print)
        if new_path != None and (shortest == None or lt(new_path, shortest)):
            shortest = new_path
    return shortest


def shortest_path(graph, start, end, to_print=False):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    lt = lambda x, y: len(x) < len(y)
    return DFS(graph, start, end, lt, [], None, to_print)

def test_SP():
    nodes = []
    for name in range(6):
        nodes.append(Node(str(name)))
    g = Digraph()
    for n in nodes:
        g.add_node(n)
    g.add_edge(Edge(nodes[0], nodes[1]))
    g.add_edge(Edge(nodes[1], nodes[2]))
    g.add_edge(Edge(nodes[2], nodes[3]))
    g.add_edge(Edge(nodes[2], nodes[4]))
    g.add_edge(Edge(nodes[3], nodes[4]))
    g.add_edge(Edge(nodes[3], nodes[5]))
    g.add_edge(Edge(nodes[0], nodes[2]))
    g.add_edge(Edge(nodes[1], nodes[0]))
    g.add_edge(Edge(nodes[3], nodes[1]))
    g.add_edge(Edge(nodes[4], nodes[0]))
    sp = shortest_path(g, nodes[0], nodes[5], to_print=True)
    print('Shortest path found by DFS:', print_path(sp))
test_SP()


def lightest_path(graph, start, end, to_print=False):
    """Assumes graph is a Digraph; start and end are nodes"""
    def lt(a, b):
        weight_a = 0
        for e in a:
            weight_a += e.get_weight()
        weight_b = 0
        for e in b:
            weight_b += e.get_weight()
        return weight_a < weight_b
    return DFS(graph, start, end, lt, [], None, to_print)

def test_LP():
    nodes = []
    for name in range(4):
        nodes.append(Node(str(name)))
    g = Digraph()
    for n in nodes:
        g.add_node(n)
    g.add_edge(Weighted_edge(nodes[0], nodes[1], 10))
    g.add_edge(Weighted_edge(nodes[0], nodes[2], 20))
    g.add_edge(Weighted_edge(nodes[1], nodes[3], 10))
    g.add_edge(Weighted_edge(nodes[2], nodes[3], 20))
    lp = lightest_path(g, nodes[0], nodes[3], to_print=True)
    print('Lightest path found by DFS:', print_path(lp))
test_LP()