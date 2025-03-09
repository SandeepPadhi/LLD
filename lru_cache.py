import unittest

class Node:
    def __init__(self,key,value):
        self.next=None 
        self.prev=None 
        self.key=key 
        self.value=value 

class LRU:
    def __init__(self,capacity):
        self.cache={}
        self.left=Node(-1,-1)
        self.right=Node(-1,-1)
        self.left.next=self.right 
        self.right.prev=self.left 
        self.capacity=capacity
    

    def _remove(self,node):
        prev=node.prev 
        nxt=node.next
        prev.next=nxt 
        nxt.prev=prev
    
    def _insert(self,node):
        prev=self.right.prev 
        prev.next=node
        node.prev=prev 
        node.next=self.right 
        self.right.prev=node
    
    def get(self,key):
        if key not in self.cache:
            return -1 
        
        node=self.cache[key]
        self._remove(node)
        self._insert(node)
        return node.value
    
    def put(self,key,value):
        if key in self.cache:
            node=self.cache[key]
            self._remove(node)
            del self.cache[key]
        node=Node(key,value)
        self.cache[key]=node
        self._insert(node)

        if len(self.cache) > self.capacity:
            print("ues")
            node=self.left.next 
            self._remove(node)
            del self.cache[node.key]    



class TestLRU(unittest.TestCase):
    def testlru(self):
        capacity=4
        lru=LRU(capacity)
        lru.put(1,3)
        lru.put(2,3)
        lru.put(3,4)
        lru.put(2,4)
        lru.put(5,5)
        node=lru.left 
        while node:
            print(f"key:{node.key} value:{node.value}")
            node=node.next
        self.assertEqual((lru.right.prev.key,lru.right.prev.value),(5,5))
        self.assertEqual(lru.get(2),4)


if __name__ == "__main__":
    unittest.main()

