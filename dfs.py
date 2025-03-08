import unittest

def dfs_interactive(graph,start_node):
    visited=[start_node]
    stack=[start_node]

    while stack:
        node=stack.pop()
        print(f"node:{node}")
        for neighbor in reversed(graph.get(node,[])):
            if neighbor not in visited:
                visited.append(neighbor)
                stack.append(neighbor)
            
    return visited 


def dfs_recursive(graph,visited,stack):
    if not stack:
        return visited 
    
    node=stack.pop()
    print(f"node:{node}")

    for neighbor in reversed(graph.get(node,[])):
        if neighbor not in visited:
            visited.append(neighbor)
            stack.append(neighbor)
            
    return dfs_recursive(graph,visited,stack)
    
        




graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_node='A'



class TestDFS(unittest.TestCase):
    def testdfs(self):
        visited1=dfs_interactive(graph,start_node)
        print(f"visited1 :{visited1}")
        visited2=dfs_recursive(graph,[start_node],[start_node])
        print(f"visited2:{visited2}")
        self.assertEqual(visited1,visited2)

if __name__ == "__main__":
    unittest.main()
