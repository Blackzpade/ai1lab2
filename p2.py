class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class LeftSkewedTree:
    def __init__(self):
        self.root = None

    def create_left_skewed_tree(self, values):
        if not values:
            return
        self.root = TreeNode(values[0])
        current = self.root
        for value in values[1:]:
            current.left = TreeNode(value)
            current = current.left

    def print_tree(self, node):
        if node is not None:
            print(node.value, end=' ')
            self.print_tree(node.left)

class BalancedTree:
    def __init__(self):
        self.root = None

    def sorted_array_to_bst(self, values):
        if not values:
            return None
        mid = len(values) // 2
        node = TreeNode(values[mid])
        node.left = self.sorted_array_to_bst(values[:mid])
        node.right = self.sorted_array_to_bst(values[mid + 1:])
        return node

    def create_balanced_tree(self, values):
        sorted_values = sorted(values)
        self.root = self.sorted_array_to_bst(sorted_values)

    def print_tree(self, node):
        if node is not None:
            self.print_tree(node.left)
            print(node.value, end=' ')
            self.print_tree(node.right)

def search_tree(node, value):
    if node is None:
        return 0  # Not found
    comparisons = 1
    if value == node.value:
        return comparisons
    elif value < node.value:
        return comparisons + search_tree(node.left, value)
    else:
        return comparisons + search_tree(node.right, value)

def main():
    size = int(input("Enter the size of the left-skewed binary tree (minimum 4): "))
    if size < 4:
        print("Error: Size must be at least 4.")
        return

    values = []
    for i in range(size):
        val = int(input(f"Enter value {i + 1}: "))
        values.append(val)

    # Create Left-Skewed Tree
    left_skewed_tree = LeftSkewedTree()
    left_skewed_tree.create_left_skewed_tree(values)

    # Create Balanced Tree
    balanced_tree = BalancedTree()
    balanced_tree.create_balanced_tree(values)

    # Print both trees
    print("\nLeft-Skewed Tree (Pre-order):")
    left_skewed_tree.print_tree(left_skewed_tree.root)

    print("\nBalanced Tree (In-order):")
    balanced_tree.print_tree(balanced_tree.root)

    # Search for values
    search_value1 = int(input("\nEnter the first value to search: "))
    search_value2 = int(input("Enter the second value to search: "))

    comparisons_left_skewed_1 = search_tree(left_skewed_tree.root, search_value1)
    comparisons_left_skewed_2 = search_tree(left_skewed_tree.root, search_value2)

    comparisons_balanced_1 = search_tree(balanced_tree.root, search_value1)
    comparisons_balanced_2 = search_tree(balanced_tree.root, search_value2)

    print(f"\nComparisons in Left-Skewed Tree for {search_value1}: {comparisons_left_skewed_1}")
    print(f"Comparisons in Left-Skewed Tree for {search_value2}: {comparisons_left_skewed_2}")
    print(f"Comparisons in Balanced Tree for {search_value1}: {comparisons_balanced_1}")
    print(f"Comparisons in Balanced Tree for {search_value2}: {comparisons_balanced_2}")

if __name__ == "__main__":
    main()
