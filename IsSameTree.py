"""
    Platform: LeetCode

    Link to Problem: https://leetcode.com/problems/same-tree/

    Problem Statement: Given the roots of two binary trees p and q, write a function to check if they are the same or not.
    Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

    Example 1:

                    1                   1
                2       3           2       3

    Input: p = [1,2,3], q = [1,2,3]
    Output: true

    Example 2:

                    1                   1
                2                           2

    Input: p = [1,2], q = [1,null,2]
    Output: false

    Example 3:

    Input: p = [1,2,1], q = [1,1,2]
    Output: false    

    Constraints:

    The number of nodes in both trees is in the range [0, 100].
    -104 <= Node.val <= 104
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SameTree:
    def __init__(self) -> None:
        pass

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        if p is None and q is None:
            return True
        elif p is not None and q is not None:
            pass
        else:
            return False
        
        if p.val != q.val:
            return False
        
        isSameLeftSubTree = self.isSameTree(p.left, q.left)
        isSameRightSubTree = self.isSameTree(p.right, q.right)
        
        return isSameLeftSubTree and isSameRightSubTree

# Code to construct Binary Tree from array InOrder fashion
class Tree:
    # Function to insert nodes in level order
    def insertLevelOrder(self, arr, root, i, n):        
        # Base case for recursion
        if i < n:
            temp = TreeNode(arr[i])
            root = temp
    
            # insert left child
            root.left = self.insertLevelOrder(arr, root.left, 2 * i + 1, n)
    
            # insert right child
            root.right = self.insertLevelOrder(arr, root.right, 2 * i + 2, n)

        return root
    
    # Function to print tree nodes in
    # InOrder fashion
    def inOrder(self, root):
        if root != None:
            self.inOrder(root.left)
            print(root.data, end = " ")
            self.inOrder(root.right)

tree1_arr = [1, 2, 3]
tree2_arr = [1, 2, 3]

tree = Tree()

root1 = None
root1 = tree.insertLevelOrder(tree1_arr, root1, 0, len(tree1_arr))

root2 = None
root2 = tree.insertLevelOrder(tree2_arr, root2, 0, len(tree2_arr))

sameTreeObj = SameTree()
print(sameTreeObj.isSameTree(root1, root2))
        
    