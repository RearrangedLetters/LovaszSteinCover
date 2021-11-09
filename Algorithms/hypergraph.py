class Hypergraph:
    hEdges = list()

    def __init__(self, hEdges):
        self.hEdges = hEdges

    def get_points(self):
        s = set()
        for e in self.hEdges:
            for x in e:
                s.add(x)
        return s

    def num_points(self):
        return len(self.get_points())

    def get_hedges(self):
        return self.hEdges

    def num_hedges(self):
        return len(self.hEdges)

    def print(self):
        print(self.hEdges)
