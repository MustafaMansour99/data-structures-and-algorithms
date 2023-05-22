class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

"this calss for treverse tree by in order or pre-order or post-order  "
class BinaryTree:
    def __init__(self):
        self.root = None

    def traverse_inorder(self, node):
        if node is None:
            return []
        left_values = self.traverse_inorder(node.left)
        right_values = self.traverse_inorder(node.right)
        return left_values + [node.value] + right_values

    def traverse_preorder(self, node):
        if node is None:
            return []
        left_values = self.traverse_preorder(node.left)
        right_values = self.traverse_preorder(node.right)
        return [node.value] + left_values + right_values
    
    def traverse_postorder(self, node):
        if node is None:
            return []
        left_values = self.traverse_preorder(node.left)
        right_values = self.traverse_preorder(node.right)
        return  left_values + right_values + [node.value]
    
    """
    this function returns the maximum value in binary tree
    """

    def find_maximum_value(self):
        if self.root is None:
            return "Tree is Empty!!"
        return self._find_maximum_value_helper(self.root)
    def _find_maximum_value_helper(self, node):
        if node is None:
            return None
        max_value = node.value
        left_max = self._find_maximum_value_helper(node.left)
        if left_max is not None and left_max > max_value:
            max_value = left_max
        right_max = self._find_maximum_value_helper(node.right)
        if right_max is not None and right_max > max_value:
            max_value = right_max

        return max_value
        
    
        
"this class for serach in tree using binary search tree and check if value bigger than node add to right of the node and if it smaller add to the left side of the node and have a function to check if the value is inside in tree or not "
class BinarySearchTree(BinaryTree):
    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        if self.root is None:
            return "Tree is empty"

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add_recursive(self.root, value)

    def _add_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._add_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._add_recursive(node.right, value)
    def contains(self,value):
        tree=self.traverse_preorder(self.root) or self.traverse_postorder(self.root) or self.traverse_inorder(self.root)
        if value in tree:
            return True
        else:
            return False



bst = BinarySearchTree()
bst.add(5)
bst.add(2)
bst.add(1)
bst.add(2)
bst.add(7)
bst.add(1)
bst.add(3)
bst.add(6)
bst.add(8)
bst.add(10)
bst.add(4)
print(bst.traverse_postorder(bst.root))
print(bst.contains(7))
max_value =bst.find_maximum_value()
print("Maximum value:", max_value)

