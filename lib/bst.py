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

    def print_tree(self, order=None):
        if order == "inorder":
            self.print_inorder()
        if order == "preorder":
            self.print_preorder()
        if order == "postorder":
            self.print_postorder()
            
    def print_inorder(self):
        if self.right:
            self.right.print_inorder()

        print self.value

        if self.left:
            self.left.print_inorder()

    def print_preorder(self):
        print self.value

        if self.right:
            self.right.print_preorder()

        if self.left:
            self.left.print_preorder()

    def print_postorder(self):
        if self.right:
            self.right.print_postorder()

        if self.left:
            self.left.print_postorder()

        print self.value
        
    def find_min(self, parent):
        if self.right:
            return self.right.find_min(self)
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

    def find_height(self):
        if self.right:
            height_right = self.right.find_height()
        else:
            height_right = 0
        if self.left:
            height_left = self.left.find_height()
        else:
            height_left = 0

        return 1 + max(height_left, height_right)

    def count_leaf_nodes(self):
        if self.right == None and self.left == None:
            return 1
        
        if self.right:
            right_count = self.right.count_leaf_nodes()
        else:
            right_count  = 0
        if self.left:
            left_count = self.left.count_leaf_nodes()
        else:
            left_count = 0
            
        return right_count + left_count

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
                    parent.left = succ.left
                else:
                    parent.right = succ.left

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

    def print_tree(self, order=None):
        if self.root:
            if order == None:
                self.root.print_tree(order="inorder")
            else:
                self.root.print_tree(order)

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

    def find_height(self):
        if self.root == None:
            return 0

        return self.root.find_height()

    def count_leaf_nodes(self):
        if self.root == None:
            return 0

        return self.root.count_leaf_nodes()
