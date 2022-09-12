class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        hashmap = {}#一个存储clone过的点的工具/记录
        #因为不是所有的图都有环/回到起点，所以需要积累下来起点在哪(<-clone()会回到第一层)
        def clone(node):
            if node in hashmap:
                return hashmap[node]
            hashmap[node] = Node(node.val)
            for nbs in node.neighbors:
                hashmap[node].neighbors.append(clone(nbs))#这个被clone过的点的邻居也必须是clone过的点
            return hashmap[node]#以node为起点的图（内部结构已经构建好了）
        
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