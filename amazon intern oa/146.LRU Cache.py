"""
Method1: double linked list + hashmap
"""
class Node:
    
    def __init__(self, key=0, value=0):
        self.key = key
        self.val = value
        self.pre = self.next = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        #left->lru, right->mru
        self.left, self.right = Node(), Node()
        #they have to be double list
        self.left.next, self.right.pre = self.right, self.left

    def remove(self, node):
        node.pre.next, node.next.pre = node.next, node.pre # !node.next.pre(instead of node.next.next) -> node.pre
        
    def insert(self, node):
        self.right.pre.next, node.pre = node, self.right.pre
        self.right.pre, node.next = node, self.right
        
    def get(self, key: int) -> int:
        if key in self.cache:
            #inorder to set current key-value pair as mru
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

"""
Method2: OrderedDict
"""
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = collections.OrderedDict()
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)#shift the most recent used to the last 
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            if len(self.cache) == self.cap:
                self.cache.popitem(last=False)# pop the first one(leat recent used)
            self.cache[key] = value
        
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)