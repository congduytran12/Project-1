#PYTHON 
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    return root

def pre_order(root):
    if root is not None:
        print(root.key, end=' ')
        pre_order(root.left)
        pre_order(root.right)

root = None
while True:
    try:
        line = input().strip()
        if line == "#":
            break
        command, key = line.split()
        if command == "insert":
            key = int(key)
            root = insert(root, key)
    except EOFError:
        break

pre_order(root)
