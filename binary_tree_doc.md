## Binary Tree
A tree whose element have at most 2 children is called a binary tree.

### Binary Tree Representation
A tree is represented by a pointer to the topmost node of the tree. If the tree is empty, then the value of the root is NULL.
A Tree node contains the following parts.
- Data
- Pointer to the left child
- Pointer to the right child.

```
class BinaryTreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
```

### Basic Operation on Binary Tree
- Inserting an element
- Removing an element
- Searching for an element
- Traversing an element. 
    - PreOrder Traversal \
    Here, the traversal is: root - left child - right child. It means that the root node is traversed first then its left child and finally the right child.

    - InOrder Traversal \
    Here, the traversal is : left child - root - right child. It means that the left child is traversed first then its root node and finally the right child.

    - PostOrder Traversal \
    Here, the traversal is: left child - right child - root. It means that the left child is traversed first then the right child and finally its rood node.


### Tree


                 1 //Root Node
                / \
               2    3
              / \  / \
             4  5  6  7 //Leaf Nodes

PreOrder Traversal of the above tree: 1-2-4-5-3-6-7 \
InOrder Traversal of the above tree: 4-2-5-1-6-3-7 \
PostOrder Traversal of the above tree: 4-5-2-6-7-3-1 

## Properties of Binary Tree

1. The maximum number of nodes at level 'l' of a binary tree is 2<sup>l</sup>.
2. The maximum number of nodes in a binary tree of height 'h' is 2<sup>h+1</sup> - 1.
3. In a Binary Tree with N nodes, minimum possible height or the minimum number of levels is log<sub>2</sub>(N+1)
4. A Binary Tree with L leaves has at least | Log<sub>2</sub>L | +1 levels.
5. In a Binary Tree where every node has 0 or 2 children, the number of leaf nodes is always one more than nodes with two children.
6. In a non empty binary tree, if n is the total number of nodes and e is the total number of edges, then e=n-1

### Types of Binary Trees:

#### Full Binary Tree:
A Binary Tree is a full binary tree if every node has 0 or 2 children.

             18
           /    \  
         15      30  
        /  \    /  \
      40    50 100   40

             18
           /    \   
         15     20    
        /  \       
      40    50   
     /   \
    30   50

               18
            /     \  
          40       30  
                   /  \
                 100   40

#### Complete Binary Tree:
A Binary Tree is a Complete Binary tree if all the levels are completely filled except possibly the last level and the last level has all keys as left as possible.

A complete binary tree is just like a full binary tree, but with two major differences:

- Every level must be completely filled
- All the leaf elements must lean towards the left.
- The last leaf element might not have a right sibling i.e. a complete binary tree doesn’t have to be a full binary tree.

The following are examples of Complete Binary Trees.

             18
           /     \  
         15       30  
        /  \     /  \
      40    50 100   40


             18
           /     \  
         15       30  
        /  \      /  \
      40    50  100   40
     /  \   /
    8   7  9 

Practical example of Complete Binary Tree is Binary Heap. 

#### Perfect Binary Tree:
A Binary tree is a Perfect Binary Tree in which all the internal nodes have two children and all leaf nodes are at the same level. 

The following are the examples of Perfect Binary Trees. 

              18
           /      \  
         15        30  
        /  \      /  \
      40    50  100   40


             18
           /    \  
         15      30  

In a Perfect Binary Tree, the number of leaf nodes is the number of internal nodes plus 1

A Perfect Binary Tree of height h (where the height of the binary tree is the number of edges in the longest path from the root node to any leaf node in the tree, height of root node is 0) has 2h+1 – 1 node. 

#### Balanced Binary Tree:
A Binary tree is balanced if the height of the tree is O(Log n) where n is the number of nodes. For Example, the AVL tree maintains O(Log n) height by making sure that the difference between the heights of the left and right subtrees is at most 1. 


#### A degenerate (or pathological) tree:
A degenerate or pathological tree is the tree having a single child either left or right.

      10
      /
    20
     \
     30
      \
      40     

#### Skewed Binary Tree:
A skewed binary tree is a pathological/degenerate tree in which the tree is either dominated by the left nodes or the right nodes. Thus, there are two types of skewed binary tree: left-skewed binary tree and right-skewed binary tree.

              10                           10                                         
             /                              \
            20                               20
           /                                  \
         30                                    30
        /                                       \
       40                                        40
    Left-Skewed Binary Tree                   Right-Skewed Binary Tree

### Tree Traversal
               1
             /   \
            2     3
          /   \
         4     5

    Depth First Traversals:
        (a) Preorder (Root, Left, Right)  : 1 2 4 5 3  
        (b) Inorder (Left, Root, Right)   : 4 2 5 1 3 
        (c) Postorder (Left, Right, Root) : 4 5 2 3 1 
    
    Breadth-First or Level Order Traversal: 1 2 3 4 5 

#### Preorder Traversal:
    Algorithm Preorder(tree)
        1. Visit the root.
        2. Traverse the left subtree, i.e., call Preorder(left-subtree)
        3. Traverse the right subtree, i.e., call Preorder(right-subtree) 

Uses of Preorder \
Preorder traversal is used to create a copy of the tree. Preorder traversal is also used to get prefix expression on an expression tree.

#### Inorder Traversal:
    Algorithm Inorder(tree)
        1. Traverse the left subtree, i.e., call Inorder(left-subtree)
        2. Visit the root.
        3. Traverse the right subtree, i.e., call Inorder(right-subtree)

Uses of Inorder \
In the case of binary search trees (BST), Inorder traversal gives nodes in non-decreasing order. To get nodes of BST in non-increasing order, a variation of Inorder traversal where Inorder traversal s reversed can be used. 

#### Postorder Traversal:
    Algorithm Postorder(tree)
        1. Traverse the left subtree, i.e., call Postorder(left-subtree)
        2. Traverse the right subtree, i.e., call Postorder(right-subtree)
        3. Visit the root.

Uses of Postorder \
Postorder traversal is used to delete the tree. Postorder traversal is also useful to get the postfix expression of an expression tree. Please see