class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def addNode(root, data):
    if root==None:
        return Node(data)
    else:
        if root.data>data:
            root.left = addNode(root.left, data)
        if root.data>data:
            root.right = addNode(root.right, data)

def inorder(root):
    if root


root = Node(30)
addNode(root, 40)
addNode(root, 20)
addNode(root, 10)
addNode(root, 25)

