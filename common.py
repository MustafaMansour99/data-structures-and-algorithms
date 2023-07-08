class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def tree_intersection(tree1, tree2):
    def traverse_tree(node, values):
        if node is None:
            return

        values.add(node.val)
        traverse_tree(node.left, values)
        traverse_tree(node.right, values)

    values_set = set()
    traverse_tree(tree1, values_set)

    common_values = set()

    def find_common_values(node):
        if node is None:
            return

        if node.val in values_set:
            common_values.add(node.val)

        find_common_values(node.left)
        find_common_values(node.right)

    find_common_values(tree2)
    return common_values

#to be 

tree1 = TreeNode(5)
tree1.left = TreeNode(2)
tree1.right = TreeNode(7)
tree1.left.left = TreeNode(1)
tree1.left.right = TreeNode(3)

tree2 = TreeNode(7)
tree2.left = TreeNode(2)
tree2.right = TreeNode(10)
tree2.left.left = TreeNode(3)
tree2.left.right = TreeNode(8)

# Call the tree_intersection function
common_values = tree_intersection(tree1, tree2)

print(common_values)  # Output: {2, 3, 7}