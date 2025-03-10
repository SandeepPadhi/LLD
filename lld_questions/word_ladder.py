import unittest
from collections import defaultdict

begin_word="hit"
end_word="cog"

wordlist=["hot","dot","dog","lot","log","cog"]
wordlist.append(begin_word)

graph=defaultdict(list)

def is_connected(word1,word2):
    count=0
    for a,b in zip(word1,word2):
        if a!=b:
            count+=1
    return count==1
    


for word1 in wordlist:
    for word2 in wordlist:
        if is_connected(word1,word2):
            graph[word1].append(word2)



def bfs(start_node,end_node):
    from collections import deque
    queue=deque([(start_node,0)])
    visited=set([start_node])
    
    while queue:
        node,distance=queue.popleft()
        if node==end_node:
            return distance
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor,distance+1))
    return -1


class TestWordLadder(unittest.TestCase):
    def test_word_ladder(self):
        start_node="hit"
        end_node="cog"
        self.assertEqual(bfs(start_node,end_node)+1,5)


if __name__ == "__main__":
    unittest.main()


