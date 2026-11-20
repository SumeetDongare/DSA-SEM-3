
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    new_node = Node(data)

    if root is None:
        return new_node

    queue = [root]

    while queue:
        current = queue.pop(0)

        if current.left is None:
            current.left = new_node
            return root
        else:
            queue.append(current.left)

        if current.right is None:
            current.right = new_node
            return root
        else:
            queue.append(current.right)


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


root = None

value = list(map(int, input("Enter values to insert into the binary tree (space-separated): ").split()))
for val in value:
    root = insert(root, val)

print("In-order:")
inorder(root)

print("\nPre-order:")
preorder(root)

print("\nPost-order:")
postorder(root)
