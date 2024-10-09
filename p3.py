
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_node(root, value):
    if root is None:
        return TreeNode(value)
    else:
        if value < root.value:
            root.left = insert_node(root.left, value)
        else:
            root.right = insert_node(root.right, value)
    return root

def inorder_traversal(root):
    stack = []
    current = root
    traversal = []

    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            traversal.append(current.value)
            current = current.right
        else:
            break

    return traversal

def preorder_traversal(root):
    stack = []
    current = root
    traversal = []

    while True:
        if current is not None:
            traversal.append(current.value)
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            current = current.right
        else:
            break

    return traversal

def postorder_traversal(root):
    stack = []
    current = root
    traversal = []
    while True:
        while current is not None:
            if current.right is not None:
                stack.append(current.right)
            stack.append(current)
            current = current.left
        current = stack.pop()
        if current.right is not None and stack and stack[-1] == current.right:
            temp = stack.pop()
            stack.append(current)
            current = temp
        else:
            traversal.append(current.value)
            current = None
        if not stack:
            break

    return traversal

def print_tree(root, level=0):
    if root is not None:
        print_tree(root.right, level + 1)
        print(' ' * 4 * level + '->', root.value)
        print_tree(root.left, level + 1)

def main():
    root = None
    num_nodes = int(input("Enter the number of nodes: "))

    for _ in range(num_nodes):
        value = int(input("Enter node value: "))
        root = insert_node(root, value)

    print("Tree Structure:")
    print_tree(root)
    print("\nInorder Traversal:", inorder_traversal(root))
    print("Preorder Traversal:", preorder_traversal(root))
    print("Postorder Traversal:", postorder_traversal(root))

if __name__ == "__main__":
    main()
