
"""
This is a linked list data structure. 
"""

class Node:

    #initialize function for init data
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None

    #print link data
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

if __name__ == '__main__':
    linkedList = LinkedList()

    #crate node
    linkedList.head = Node(1)
    node1 = Node(5)
    node2  = Node(10)
    node3 = Node(435)

    #link to the all node
    linkedList.head.next = node1
    node1.next = node2
    node2.next = node3

    linkedList.printList()

