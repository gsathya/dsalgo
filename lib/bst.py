class Node:
    def __init__(self, value=None):
        self.value = value
        self.right = None
        self.left = None

    def add(self, value):
        # check if we already have the value
        if self.value == value:
            self.value = value

        # move right if value is smaller
        elif self.value > value:
            if self.right == None:
                self.right = Node(value)
            else:
                self.right.add(value)

        # move left if value is greater
        else:
            if self.left == None:
                self.left = Node(value)
            else:
                self.left.add(value)

    def print_tree(self):
        if self.right:
            self.right.print_tree()

        print self.value

        if self.left:
            self.left.print_tree()

    def delete(self, value):
        if self.value == value:
            del

class BST:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.root.add(value)

    def print_tree(self):
        if self.root:
            self.root.print_tree()

    def find_min(self):
        root = self.root

        if root == None:
            return
        
        while root.right != None:
            root = root.right

        print root.value

    def delete(self, value):
        if self.root == None:
            return

        self.root.delete(value)
        
if __name__ == "__main__":
    bst = BST()
    bst.add(4)
    bst.add(3)
    bst.add(3)
    bst.add(5)
    bst.add(7)
    bst.add(8)
    bst.add(2)
    bst.print_tree()
    bst.find_min()
