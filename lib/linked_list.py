class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            head = self.head
            while head.next != None:
                head = head.next
            node = Node(value)
            head.next = node

    def find(self, value):
        if not self.head:
            return None
        else:
            head = self.head
            while head != None:
                if head.value == value:
                    return head
                else:
                    head = head.next

    def print_list(self):
        if not self.head:
            return None
        else:
            head = self.head
            while head != None:
                print head.value
                head = head.next

    def reverse(self):
        if not self.head:
            return
        else:
            head = self.head
            temp = None
            prev = None
            while head != None:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            
            self.head = prev

def print_rev(head):
    if head:
        print_rev(head.next)
        print head.value
