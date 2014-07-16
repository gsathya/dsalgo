"""
Return the middle element in linked list
"""

import linked_list

llist = linked_list.LinkedList()
for i in range(10):
    llist.insert(i)

i = 0
j = 0

llist_dup = linked_list.LinkedList()
for i in range(10):
    llist_dup.insert(i)


# breaks for odd numbs probably
while(llist_dup.head.next.next != None):
    llist.head = llist.head.next
    j = llist.head.value
    llist_dup.head = llist_dup.head.next.next
        
print j

