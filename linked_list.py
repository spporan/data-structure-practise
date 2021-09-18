
"""
This is a linked list data structure. 
"""



class Node:
    """
    An object for storing a single node of a linked list
    Models have two attribute one is store data and another link to the next node.
    Keeping referrence to the next node.
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    
    """Had is a Starting point of linkedlist"""
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    """get Size of the linked list"""
    def size(self):
        count = 0
        current_node = self.head

        while current_node:
            count += 1
            current_node = current_node.next

        return count


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
    len = linkedList.size()
    print("Empty list :", linkedList.is_empty())
    print("size of list : ", len)

