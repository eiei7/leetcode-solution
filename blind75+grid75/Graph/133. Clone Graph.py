class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        hashmap = {}
        def clone(node):
            if node in hashmap:
                return hashmap[node]
            hashmap[node] = Node(node.val)
            for nbs in node.neighbors:
                hashmap[node].neighbors.append(clone(nbs))
            return hashmap[node]
        
        return clone(node) if node else None

#TC:O(n)
#SC:O(n)

"""
What in hashmap?
{<__main__.Node object at 0x7fb3e777ebc0>: <__main__.Node object at 0x7fb3e777f9a0>, <__main__.Node object at 0x7fb3e777ebf0>: <__main__.Node object at 0x7fb3e777fc70>, <__main__.Node object at 0x7fb3e777efb0>: <__main__.Node object at 0x7fb3e77bb700>, <__main__.Node object at 0x7fb3e777f160>: <__main__.Node object at 0x7fb3e77bb790>}
{<__main__.Node object at 0x7fb3e777ebc0>: <__main__.Node object at 0x7fb3e777f9a0>, <__main__.Node object at 0x7fb3e777ebf0>: <__main__.Node object at 0x7fb3e777fc70>, <__main__.Node object at 0x7fb3e777efb0>: <__main__.Node object at 0x7fb3e77bb700>, <__main__.Node object at 0x7fb3e777f160>: <__main__.Node object at 0x7fb3e77bb790>}
{<__main__.Node object at 0x7fb3e777ebc0>: <__main__.Node object at 0x7fb3e777f9a0>, <__main__.Node object at 0x7fb3e777ebf0>: <__main__.Node object at 0x7fb3e777fc70>, <__main__.Node object at 0x7fb3e777efb0>: <__main__.Node object at 0x7fb3e77bb700>, <__main__.Node object at 0x7fb3e777f160>: <__main__.Node object at 0x7fb3e77bb790>}
{<__main__.Node object at 0x7fb3e777ebc0>: <__main__.Node object at 0x7fb3e777f9a0>, <__main__.Node object at 0x7fb3e777ebf0>: <__main__.Node object at 0x7fb3e777fc70>, <__main__.Node object at 0x7fb3e777efb0>: <__main__.Node object at 0x7fb3e77bb700>, <__main__.Node object at 0x7fb3e777f160>: <__main__.Node object at 0x7fb3e77bb790>}
"""
