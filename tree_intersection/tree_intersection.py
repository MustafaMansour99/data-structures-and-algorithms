from Tree.Node import Node
from Tree.Tree import Tree
"""this function takes two binary trees as arguments and check if tree is None or not."""
def tree_intersection(tree1, tree2):
    hashmap1={}
    hashmap2={}
    out_list=[]
    if tree1.root is None or tree2.root is None:
        return "Empty Trees"
    else:
        iterate_trees(tree1,hashmap1)
        iterate_trees(tree2,hashmap2)
    for i in hashmap1:
        if i in hashmap2:
            out_list.append(i)
    return out_list
def iterate_trees(inp_tree,hashmap):
    """this function iterates on the trees nodes and append values to a hashmap"""
    if inp_tree.root.left:
        tree=Tree()
        tree.root=inp_tree.root.left
        iterate_trees(tree,hashmap)
    if inp_tree.root.right:
        tree=Tree()
        tree.root=inp_tree.root.right
        iterate_trees(tree,hashmap)
    if(inp_tree.root.val in hashmap):
            hashmap[inp_tree.root.val]+=1
    else:
            hashmap[inp_tree.root.val]=1 