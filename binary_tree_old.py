from binary_tree_node import *

class BinaryTree:

    # def __init__(self, *args) is a constructor that initializes 
    # the data members of BinaryTree
    def __init__(self, *args):
        if len(args) < 1:
            self.root = None
        elif isinstance(args[0], int):
            self.root = BinaryTreeNode(args[0])
        else:
            self.root = None
            for x in args[0]:
                self.insert(x)

    # insert_bt inserts a given key into the binary tree
    # insert_bt is used for normal binary tree level by level insertion
    def insert_bt(self, key):
        temp_queue = []
        temp = self.root

        temp_queue.append(temp)

        while temp_queue:
            temp = temp_queue[0]
            temp_queue.pop(0)

            if not temp.left:
                temp.left = BinaryTreeNode(key)
                break
            else:
                temp_queue.append(temp.left)

            if not temp.right:
                temp.right = BinaryTreeNode(key)
                break
            else:
                temp_queue.append(temp.right)

    # insert inserts an integer into the binary search tree
    def insert(self, node_data):
        new_node = BinaryTreeNode(node_data)
        if not self.root:
            self.root = new_node
        else:
            parent = None
            temp_pointer = self.root
            while temp_pointer:
                parent = temp_pointer
                if node_data <= temp_pointer.data:
                    temp_pointer = temp_pointer.left
                else:
                    temp_pointer = temp_pointer.right
            if node_data <= parent.data:
                parent.left = new_node
            else:
                parent.right = new_node

    # find_in_bst_rec is a helper function used by find_in_bst to 
    # find the given data in the binary search tree
    def find_in_bst_rec(self, node, node_data):
        if not node:
            return None
        if node.data == node_data:
            return node
        elif node.data > node_data:
            return self.find_in_bst_rec(node.left, node_data)
        else:
            return self.find_in_bst_rec(node.right, node_data)

    # find_in_bst is used to find the given data in the binary search tree
    def find_in_bst(self, node_data):
        return self.find_in_bst_rec(self.root, node_data)

    # populate_parents_rec is a helper function that is used by populate_parents
    def populate_parents_rec(self, node, parent):
        if node:
            node.parent = parent
            self.populate_parents_rec(node.left, node)
            self.populate_parents_rec(node.right, node)

    # populate_parents is used to populate the parent pointers 
    # of the nodes in the BinaryTree
    def populate_parents(self):
        self.populate_parents_rec(self.root, None)

    # get_sub_tree_node_count returns the count of the nodes in 
    # the sub-tree rooted at the given node
    def get_sub_tree_node_count(self, node):
        if not node:
            return 0
        else:
            return 1 + self.get_sub_tree_node_count(node.left) + self.get_sub_tree_node_count(node.right)

    # populate_count is a helper function used by populate_count 
    def populate_count_rec(self, node):
        if node:
            node.count = self.get_sub_tree_node_count(node)
            self.populate_count_rec(node.left)
            self.populate_count_rec(node.right)

    # populate_count is used to calculate the number of 
    # nodes present in the BinaryTree
    def populate_count(self):
        self.populate_count_rec(self.root)

    # get_tree_deep_copy_rec is a helper function used by get_tree_deep_copy
    def get_tree_deep_copy_rec(self, node):
        if node:
            new_node = BinaryTreeNode(node.data)
            new_node.left = self.get_tree_deep_copy_rec(node.left)
            new_node.right = self.get_tree_deep_copy_rec(node.right)
            return new_node
        else:
            return None

    # get_tree_deep_copy is used to make a deep copy of the BinaryTree
    def get_tree_deep_copy(self):
        if not self.root:
            return None
        else:
            tree_copy = BinaryTree()
            tree_copy.root = self.get_tree_deep_copy_rec(self.root)
            return tree_copy

    # find_in_BT_rec is a helper function used by find_in_BT to
    # find the given data in the binary tree 
    def find_in_BT_rec(self, node, node_data):
        if not node:
            return None

        if node.data == node_data:
            return node

        left_node = self.find_in_BT_rec(node.left, node_data)
        if left_node:
            return left_node

        right_node = self.find_in_BT_rec(node.right, node_data)
        return right_node
    
    # find_in_BT is used to find the given data in the binary tree
    def find_in_BT(self, node_data):
        return self.find_in_BT_rec(self.root, node_data)