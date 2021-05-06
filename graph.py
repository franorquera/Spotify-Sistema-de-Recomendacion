class Graph:

    def __init__(self):
        self.graph = {}
        self.vertex = 0
        self.edge = 0

    def add_vertex(self, v):
        if v in self.graph:
            return
        self.graph[v] = {}
        self.vertex += 1
    
    def vertex_amount(self):
        return self.vertex
    
    def edge_amount(self, v):
        return len(self.graph[v])

    def add_edge(self, i, f, p):
        if ((i not in self.graph) or (f not in self.graph)):
            return
        if ((i in self.graph[f]) and (f in self.graph[i])):
            return
        self.graph[i][f] = p
        self.graph[f][i] = p
        self.edge += 1

    def remove_vertex(self, v):
        range_adjacent = self.graph.pop(v, None)
        if not range_adjacent:
            return
        for adjacent in range_adjacent:
            self.graph[adjacent].pop(v, None)
            self.edge -= 1
        self.vertex -= 1 

    def remove_edge(self, i, f):
        if ((i not in self.graph) or (f not in self.graph)):
            return
        if ((i not in self.graph[f]) or (f not in self.graph[i])):
            return

        self.graph[i].pop(f, None)
        self.graph[f].pop(i, None)
        self.edge -= 1

    def are_linked(self, i, f):
        if ((i in self.graph[f]) and (f in self.graph[i])):
            return self.graph[f][i]
        return False

    def get_vertices(self):
        return [x for x in self.graph]

    def get_range(self, v):
        if v not in self.graph:
            return []
        return [x for x in self.graph[v]]

    def is_vertex(self, v):
        return (v in self.graph)
    
    def get_weight(self, i, f):
        if ((i not in self.graph) or (f not in self.graph)):
            return
        if ((i not in self.graph[f]) or (f not in self.graph[i])):
            return
        return self.graph[i][f]