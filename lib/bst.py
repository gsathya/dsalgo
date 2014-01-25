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

    def find_min(self, parent):
        if self.left:
            return self.left.find_min(self)
        else:
            return [parent, self]

    def has_value(self, value):
        if self.value == value:
            return True
        elif self.value > value:
            if self.right:
                return self.right.has_value(value)
        else:
            if self.left:
                return self.left.has_value(value)

        return False

    def delete(self, value):
        if self.value > value:
            if self.right:
                self.right = self.right.delete(value)
        elif self.value < value:
            if self.left:
                self.left = self.left.delete(value)
        else:
            if self.right and self.left:
                parent, succ = self.left.find_min(self)

                if parent.left == succ:
                    parent.left = succ.right
                else:
                    parent.right = succ.right

                succ.left = self.left
                succ.right = self.right

                return succ
            elif self.right:
                return self.right
            else:
                return self.left

        return self

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

        return root.value

    def delete(self, value):
        if self.root == None:
            return

        self.root = self.root.delete(value)

    def has_value(self, value):
        if self.root == None:
            return False

        return self.root.has_value(value)
