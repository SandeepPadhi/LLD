
from collections import deque
import unittest

def bfs_interative(graph,start_node):
    visited=set([start_node])
    queue=deque()
    queue.append(start_node)

    while queue:
        node=queue.popleft()
        print(f"node visited:{node}")
        for neighbor in graph.get(node,[]):
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
    return visited



def bfs_recursive(graph,queue,visited):
    if not queue:
        return visited 
    
    node=queue.popleft()
    print(f"node visited:{node}")
    for neighbor in graph.get(node,[]):
        if neighbor not in visited:
            queue.append(neighbor)
            visited.add(neighbor)

    return bfs_recursive(graph,queue,visited)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}



class TestBFS(unittest.TestCase):
    def testbfs(self):        
        start_node='A'
        visited1=bfs_interative(graph,start_node)
        print(f"visited interative:{visited1}")

        queue=deque([start_node])
        visited2=bfs_recursive(graph,queue,set([start_node]))
        print(f"visited recursive:{visited2}")

        self.assertEqual(visited1,visited2)
        
if __name__ == '__main__':
    unittest.main()