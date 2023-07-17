from hashtable.hashtable import HashTable
from Tree.Node import Node
from Tree.bts_tree import BinaryTree 
from Tree.Tree import Tree

def tree_intersection(tree1, tree2):
    values = set()
    hashtable = HashTable()

    def traverse(node):

        if node:
            hashtable.set(str(node.val), node.val)

            if node.left:
                traverse(node.left)

            if node.right:
                traverse(node.right)

    traverse(tree1.root)

    def traverse2(node):

        if node:
            if hashtable.has(str(node.val)):
                values.add(node.val)

    traverse2(tree2.root)

    return values  

if __name__ == "__main__":
    tree1 = BinaryTree()
    tree1.root = Node(150)
    tree1.root.left = Node(100)
    tree1.root.left.left = Node(75)
    tree1.root.left.right = Node(160)
    tree1.root.left.right.left = Node(125)
    tree1.root.left.right.right = Node(175)
    tree1.root.right = Node(250)
    tree1.root.right.left = Node(200)
    tree1.root.right.right = Node(350)
    tree1.root.right.right.left = Node(300)
    tree1.root.right.right.right = Node(500)

    tree2 = BinaryTree()
    tree2.root = Node(42)
    tree2.root.left = Node(100)
    tree2.root.left.left = Node(15)
    tree2.root.left.right = Node(160)
    tree2.root.left.right.left = Node(125)
    tree2.root.left.right.right = Node(175)
    tree2.root.right = Node(600)
    tree2.root.right.left = Node(200)
    tree2.root.right.right = Node(350)
    tree2.root.right.right.left = Node(4)
    tree2.root.right.right.right = Node(500)
    print(tree1.root)

    print(tree_intersection(tree1, tree2))
