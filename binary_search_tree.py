#created node class for creating node
class Node:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None

#inser node
def insertNode(root, key):
    if root is None:
        return Node(key)
    else:
        if root.value == key:
            return root
        elif root.value < key:
            root.right = insertNode(root.right,key)
        elif root.value > key:
            root.left = insertNode(root.left,key)
    return root

def printBSTValueByorder(root):
    if root:
        printBSTValueByorder(root.left)
        print(root.value)
        printBSTValueByorder(root.right)

# Search value using BST
#This function for search value from the tree
def search(root, key):
    if root is None:
        return 'Not Found '+ str(key)
    else:
        if root.value == key:
            return 'Found value '+str(root.value)
        elif root.value > key:
            value = search(root.left,key)
            return value
        elif root.value < key:
            value = search(root.right,key)
            return value
        else:
            return "Not found "+ str(key)


if __name__ == '__main__':
    #
    #         100
    #       /     \
    #      80     435
    #    / \     / \
    #   70 85   233 440
    #   / \     / \
    #  33  75 123 240
    #
    #
    #
    r = Node(100) # create as a root node
    r = insertNode(r,80)
    r = insertNode(r, 70)
    r = insertNode(r,435)
    r = insertNode(r,33)
    r = insertNode(r,75)
    r = insertNode(r,85)
    r = insertNode(r,233)
    r = insertNode(r,440)
    r = insertNode(r, 123)
    r = insertNode(r,240)

    printBSTValueByorder(r)

    result = search(r,44)
    print('result : '+ result)
    result1 = search(r,33)
    print('result : '+ result1)
    result2 = search(r,440)
    print('result : '+ result2)
    result3 = search(r,435)
    print('result : '+ result3)
