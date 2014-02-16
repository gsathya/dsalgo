from Queue import Queue
from lib import bst

def bst_bfs(root, item):
    if root == None:
        return -1
    
    q = Queue()
    q.put(root)
    
    while not q.empty():
        node = q.get()
        
        if node.value == item:
            return node
        
        if node.right:
            q.put(node.right)
        if node.left:
            q.put(node.left)
            
    return -1
    
    
def bst_dfs(root, item):
    if root == None:
        return -1
        
    stack = []
    
    stack.append(root)
    
    while len(stack) > 0:
        node = stack.pop()
        
        if node.value == item:
            return node
        
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return -1

def bst_dfs_recurse(root, item):
    if root == None:
        return
        
    if root.value == item:
        return root

    return bst_dfs_recurse(root.left, item) or bst_dfs_recurse(root.right, item)
