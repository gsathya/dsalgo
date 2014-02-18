prev = None

def check_bst(root):
    if not root:
        return True
        
    ans = check_bst(root.left)
    
    if ans == False:
        return False
        
    if prev and root.value < prev:
        return False

    global prev
    prev = root
    
    return check_bst(root.right)
