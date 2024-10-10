class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def create_left_skewed_tree(height):
    if height == 0:
        return None
    node = Node(height)
    node.left = create_left_skewed_tree(height - 1)
    return node

def inorder_traversal(node, arr):
    if node is not None:
        inorder_traversal(node.left, arr)
        arr.append(node.data)
        inorder_traversal(node.right, arr)

def sorted_array_to_balanced_tree(arr):
    if not arr:
        return None
    mid = len(arr) // 2
    node = Node(arr[mid])
    node.left = sorted_array_to_balanced_tree(arr[:mid])
    node.right = sorted_array_to_balanced_tree(arr[mid+1:])
    return node

def search_tree(node, target):
    comparisons = 0
    while node is not None:
        comparisons += 1
        if node.data == target:
            return comparisons
        elif node.data < target:
            node = node.right
        else:
            node = node.left
    return -1  # not found

def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level + 1)
        print('  ' * level +  '->',   str(node.data))
        print_tree(node.left, level + 1)

def main():
    height = int(input("Enter the height of the left-skewed tree (min 4): "))
    if height < 4:
        height = 4
    tree = create_left_skewed_tree(height)
    print("Left-skewed binary tree:")
    print_tree(tree)

    inorder = []
    inorder_traversal(tree, inorder)
    balanced_tree = sorted_array_to_balanced_tree(inorder)

    print("\nHeight-balanced binary search tree:")
    print_tree(balanced_tree)

    data1 = int(input("Enter the first data to search: "))
    data2 = int(input("Enter the second data to search: "))

    comparisons_left_skewed = search_tree(tree, data1) + search_tree(tree, data2)
    comparisons_balanced = search_tree(balanced_tree, data1) + search_tree(balanced_tree, data2)

    print("\nComparisons in left skewed tree:", comparisons_left_skewed)
    print("Comparisons in balanced tree:", comparisons_balanced)

if __name__ == "__main__":
    main()
