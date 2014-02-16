from Queue import Queue
from lib import bst

def print_tree(root):
    q = Queue()
    curLevel = 0
    nextLevel = 0
    
    q.put(root)
    curLevel +=1
    ans = []
    
    while not q.empty():
        node = q.get()
        curLevel -=1
        
        ans.append(node.value)
        
        if node.left:
            q.put(node.left)
            nextLevel +=1
        if node.right:
            q.put(node.right)
            nextLevel +=1
            
        if curLevel == 0:
            ans.append("\n")
            curLevel = nextLevel
            nextlevel = 0

    print ' '.join([str(i) if type(i)==int else i for i in ans])
