import unittest

from lib import linked_list

class TestEditDistance(unittest.TestCase):
    def setUp(self):
        self.llist = linked_list.LinkedList()
        
    def test_create_llist(self):
        for i in range(10):
            self.llist.insert(i)

    def test_reverse_llist(self):
        for i in range(10):
            self.llist.insert(i)

        self.llist.reverse()
