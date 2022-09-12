"""
Method1: bfs
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:

    def serialize(self, root):
        res = []
        if not root:
            return "N"
        q = deque()
        q.append(root)
        while q:
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()
                if node:
                    res.append(str(node.val))
                    q.append(node.left)
                    q.append(node.right)
                else:
                    res.append("N")
        return ",".join(res)
        

    def deserialize(self, data):
        vals = data.split(",")
        if vals[0] == "N":
            return None
        res = TreeNode(int(vals[0]))
        q = deque()
        q.append(res)
        pos = 1
        node = q.popleft()
        while pos < len(vals):
            if vals[pos] != "N":
                tmp = TreeNode(int(vals[pos]))
                node.left = tmp
                q.append(tmp)
            pos += 1
            if vals[pos] != "N":
                tmp = TreeNode(int(vals[pos]))
                node.right = tmp
                q.append(tmp)
            pos += 1
            if q:
                node = q.popleft()
        return res

#TC: O(n)
#SC: O(1)

"""
Method2: dfs
"""
class Codec:

    def serialize(self, root):
        res = []
        def dfs(node):
            if not node:
                res.append("N")
                return 
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)
        

    def deserialize(self, data):
        #['1', '2', 'N', 'N', '3', '4', 'N', 'N', '5', 'N', 'N']
        vals = data.split(",")
        self.i = 0
        
        def dfs():#no need to worry about i exceed the range of list
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
            
#TC: O(n)
#SC: O(1)
