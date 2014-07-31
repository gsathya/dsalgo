class Node:
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.value = val

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, val):
        node = Node(val)
        head = self.head

        if self.head == None:
            self.head = node
        else:
            while head.next != None:
                head = head.next

            head.next = node
            node.prev = head

    def print_list(self):
        head = self.head
        while head != None:
            print head.value
            head = head.next

if __name__ == '__main__':
    dll = DoublyLinkedList()
    for i in range(10):
        dll.insert(i)

