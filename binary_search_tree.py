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

