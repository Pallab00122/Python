class DirectedGraph:
    def __init__(self):
        self.graph={}
    
    def add_node(self,node):
        if node not in self.graph:
            self.graph[node]=[]
    def add_edge(self,u,v):
        self.add_node(u)
        self.add_node(v)
        if v not in self.graph[u]:
            self.graph[u].append(v)
    def display(self):
        print(" Graph ")
        for node , neighbors in self.graph.items():
            print(f"{node} -> {','.join(map(str,neighbors))}")

if __name__ == "__main__":
    dg = DirectedGraph()
    dg.add_edge('A', 'B')
    dg.add_edge('A', 'C')
    dg.add_edge('B', 'D')
    dg.add_edge('C', 'B')
    dg.add_node('E')

dg.display()