
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

    """get Size of the linked list. Size of linear time operation. That's mean Time complexity is O(n)"""
    def size(self):
        count = 0
        current_node = self.head

        while current_node:
            count += 1
            current_node = current_node.next

        return count
    
    """
    Adding value to the linked list using this method. That's actually a constant time operation.
    adding data to the head of that linked list.
    """
    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def append(self, data):
        """
        Add data to this linked list at the end of the list.
        First of all we find out tail of that list and linked to the new node.
        It is linear time operation thats why it's time complexity O(n)
        """
        new_node = Node(data)
        current = self.head
        prev = None
        while current:
            prev = current
            current = current.next
            if current == None:
                prev.next = new_node
    
    def insert(self, data, index = 0):
        """
        This is a insert function which actually insert values given a specific index.
        If don't give any index position then it will add default position at 0.
        It's a linear time operation. Worst case of this function will be O(n)
        """
        if index < 0 or index > self.size() - 1:
            return IndexError("IndexOutOfBound Exception")

        current = self.head
        prev = None
        count = 0
        new_node = Node(data)
        while current:
            if count == index:
                if prev == None:
                    new_node.next = current
                    self.head = new_node
                else:
                    new_node.next = prev.next
                    prev.next = new_node
                break
            
            prev = current
            current = current.next
            if current != None:
                count += 1


    def search(self, key):
        """
        This is a search function. For searching a value into the linked list.
        if found it will return True other False.
        It is a linear time operation. It will take linear time. Time complexity of this function is O(n)
        """
        current = self.head
        is_found = False
        while current:
            if current.data == key:
                is_found = True
                break
            current = current.next
        return is_found
    #print link data
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def __repr__(self):
        """
        This function is linear time operation. Time complexity of this function is O(n).
        """
        nodes = []
        current_node = self.head
        while current_node:
            nodes.append(current_node.data)
            current_node = current_node.next
        return str(nodes)

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

