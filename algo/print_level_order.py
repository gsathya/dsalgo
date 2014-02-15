from Queue import Queue
from lib import bst

def print_tree(root):
    q = Queue()
    curLevel = 0
    nextLevel = 0
    
    q.put(root)
    curLevel +=1
    
    while not q.empty():
        node = q.get()
        curLevel -=1
        
        print node.value
        
        if node.left:
            q.put(node.left)
            nextLevel +=1
        if node.right:
            q.put(node.right)
            nextLevel +=1
            
        if curLevel == 0:
            print "\n"
            curLevel = nextLevel
            nextlevel = 0
