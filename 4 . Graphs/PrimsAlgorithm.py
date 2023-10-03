import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def prim_mst(self):
        visited = [False] * self.V
        min_heap = []
        mst = []
        
        heapq.heappush(min_heap, (0, 0))  
        
        while min_heap:
            weight, vertex = heapq.heappop(min_heap)
            
            # Skip vertex if visited already
            if visited[vertex]:
                continue
            
            visited[vertex] = True
            for neighbor, edge_weight in self.graph[vertex]:
                if not visited[neighbor]:
                    heapq.heappush(min_heap, (edge_weight, neighbor))
            if vertex != 0:  
                mst.append((vertex, weight))
        
        return mst

g = Graph(5)
g.add_edge(2, 4, 5)
g.add_edge(1, 2, 6)
g.add_edge(0, 1, 4)
g.add_edge(1, 3, 9)
g.add_edge(3, 4, 9)
g.add_edge(0, 3, 6)
g.add_edge(1, 4, 5)


mst = g.prim_mst()
for edge in mst:
    print(f"Edge: {edge[0]} - Weight: {edge[1]}")
