import matplotlib.pyplot as plt

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def create_balanced_tree(values):
    if not values:
        return None
    mid = len(values) // 2
    root = TreeNode(values[mid])
    root.left = create_balanced_tree(values[:mid])
    root.right = create_balanced_tree(values[mid + 1:])
    return root

def search_node(node, target):
    comparisons = 0
    while node:
        comparisons += 1
        if node.value == target:
            return comparisons
        elif target < node.value:
            node = node.left
        else:
            node = node.right
    return comparisons

def is_balanced(node):
    def check_balance(n):
        if not n:
            return 0
        left_height = check_balance(n.left)
        if left_height == -1:  # Left subtree is not balanced
            return -1
        right_height = check_balance(n.right)
        if right_height == -1:  # Right subtree is not balanced
            return -1
        if abs(left_height - right_height) > 1:
            return -1  # Current node is not balanced
        return max(left_height, right_height) + 1

    return check_balance(node) != -1

def plot_tree(node, parent_name, graph, pos=None, level=0, width=2.0, vert_gap=0.5):
    if pos is None:
        pos = {node.value: (0, 0)}
    else:
        pos[node.value] = (pos[parent_name][0] + (1 if node.value > parent_name else -1) * width / (2 ** level), -level)

    if node.left:
        pos = plot_tree(node.left, node.value, graph, pos, level + 1, width / 2, vert_gap)
    if node.right:
        pos = plot_tree(node.right, node.value, graph, pos, level + 1, width / 2, vert_gap)

    return pos

def draw_tree(node):
    if node is None:
        return
    pos = plot_tree(node, node.value, {})
    plt.figure(figsize=(10, 5))
    plt.title('Binary Tree Representation')
    for n in pos:
        plt.text(pos[n][0], pos[n][1], str(n), ha='center', va='center', bbox=dict(boxstyle='circle', facecolor='lightblue'))

    for n in pos:
        if node.left and node.left.value == n:
            plt.plot([pos[n][0], pos[node.value][0]], [pos[n][1], pos[node.value][1]], 'k-')
        if node.right and node.right.value == n:
            plt.plot([pos[n][0], pos[node.value][0]], [pos[n][1], pos[node.value][1]], 'k-')

    plt.axis('off')
    plt.show()

def main():
    # Get user input for values
    values_input = input("Enter values for the balanced tree, separated by spaces: ")
    values = list(map(int, values_input.split()))

    # Sort values for balanced tree creation
    values.sort()

    # Create the balanced tree
    balanced_tree = create_balanced_tree(values)

    # Check if the tree is balanced
    if is_balanced(balanced_tree):
        print("The tree is balanced.")
    else:
        print("The tree is not balanced.")

    # Display the tree graphically
    draw_tree(balanced_tree)

    # Nodes to search in the tree
    node_to_search1 = int(input("Enter the first value to search: "))
    node_to_search2 = int(input("Enter the second value to search: "))

    # Search in the balanced tree
    comparisons_balanced_tree_1 = search_node(balanced_tree, node_to_search1)
    comparisons_balanced_tree_2 = search_node(balanced_tree, node_to_search2)

    # Display the search results
    print("\nComparisons in Balanced Tree:")
    print(f"Search for {node_to_search1}: {comparisons_balanced_tree_1} comparisons")
    print(f"Search for {node_to_search2}: {comparisons_balanced_tree_2} comparisons")

if __name__ == "__main__":
    main()
