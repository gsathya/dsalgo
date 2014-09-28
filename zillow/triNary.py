class Node:
    """Node class as part of tri-nary tree

    self.value  -- value of current node
    self.right  -- right node (Node)
    self.left   -- left node (Node)
    self.middle -- middle node (Node)
    """

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.middle = None

    def insert(self, value):
        """Insert a value into the tree

        Keyword arguments:
        value -- value to be inserted
        """

        # insert in the middle if value is equal to current value
        if self.value == value:
            if not self.middle:
                self.middle = Node(value)
            else:
                self.middle.insert(value)

        # go right if value is greater than current value
        if self.value < value:
            if not self.right:
                self.right = Node(value)
            else:
                self.right.insert(value)

        # go left if value is smaller than current value
        if self.value > value:
            if not self.left:
                self.left = Node(value)
            else:
                self.left.insert(value)


    def is_tri_nary(self, max, min, equal):
        """Check if tree is a valid tri-nary tree

        Keyword arguments:
        max   -- max value allowed in this subtree (int)
        min   -- min value allowed in this subtree (int)
        equal -- value of parent if current node is a middle node (int)

        Returns: boolean (True/False)
        """

        # check if value is equal
        if equal and self.value != equal:
            return False

        if self.value < min:
            return False

        if self.value > max:
            return False

        # check if middle node is valid
        is_middle_valid = True
        if self.middle:
            is_middle_valid = self.middle.is_tri_nary(max, min, self.value)

        # check if left node is valid
        is_left_valid = True
        if self.left:
            is_left_valid = self.left.is_tri_nary(self.value, min, None)

        # check if right node is valid
        is_right_valid = True
        if self.right:
            is_right_valid = self.right.is_tri_nary(max, self.value, None)

        return is_middle_valid and is_left_valid and is_right_valid
        
    def has_value(self, value):
        """Check if a node with given value exists

        Keyword arguments:
        value -- value of node (int)

        Returns: boolean (True/False)
        """

        if self.value == value:
            if self.middle:
                return self.middle.has_value(value)
            else:
                return True

        if self.value < value:
            if self.right:
                return self.right.has_value(value)

        if self.value > value:
            if self.left:
                return self.left.has_value(value)

        return False

    def find_min(self, parent):
        """Find the minimum node in parent's subtree

        Keyword arguments:
        parent -- Node

        Returns: [parent, succ]
        parent -- parent of the min node (Node)
        succ   -- min node (Node)
        """

        if self.left:
            return self.left.find_min(self)
        else:
            return [parent, self]

    def delete(self, value):
        """Delete node with value from the Tree

        Keyword arguments:
        value -- value of the node to be deleted (int)

        Exceptions: raises Exception if value isn't found
        """

        # let's go right if value is bigger
        if self.value < value:
            if not self.right:
                raise Exception("Value not found: %d" %(value))
            else:
                self.right = self.right.delete(value)

        # let's go left if value is smaller
        if self.value > value:
            if not self.left:
                raise Exception("Value not found: %d" %(value))
            else:
                self.left = self.left.delete(value)
        
        if self.value == value:
            # this node doesn't have any children, let's just delete this node
            if self.middle == None and self.left == None and self.right == None:
                return None

            # hey, we have some more nodes with the same value
            if self.middle:
                self.middle = self.middle.delete(value)
            else:
                if self.right and self.left:
                    parent, succ = self.right.find_min(self)

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

class Tree:
    """class Tree to keep track of the root

    self.root -- root node (Node)

    """

    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert a value into the tree

        Keyword arguments:
        value -- value to be inserted
        """

        if not self.root:
            self.root = Node(value)
        else:
            self.root.insert(value)

    def delete(self, value):
        """Delete node with value from the Tree

        Keyword arguments:
        value -- value of the node to be deleted (int)

        Exceptions: raises Exception if value isn't found
        """

        if self.root:
            self.root = self.root.delete(value)
        else:
            raise Exception("Can not delete from empty tree")

    def has_value(self, value):
        """Check if a node with given value exists

        Keyword arguments:
        value -- value of node (int)

        Returns: boolean (True/False)
        """

        if not self.root:
            return False
        return self.root.has_value(value)

    def is_tri_nary(self, max, min, equal):
        """Check if tree is a valid tri-nary tree

        Keyword arguments:
        max   -- max value allowed in this subtree (int)
        min   -- min value allowed in this subtree (int)
        equal -- value of parent if current node is a middle node (int)

        Returns: boolean (True/False)
        """

        if not self.root:
            return True
        return self.root.is_tri_nary(max, min, equal)
