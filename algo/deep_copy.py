class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.rand = None


def deep_copy(old):
    if not old:
        return

    old_copy = old
    root = Node(old.val)
    prev = root
    temp = None

    old = old.next

    mapping = {}
    
    while old:
        temp = Node(old.val)
        mapping[old] = temp
        
        prev.next = temp
        prev = temp
        old = old.next

    old = old_copy
    temp = root

    while old:
        temp.rand = mapping[old.rand]
        temp = temp.next
        old = old.next

    return root
