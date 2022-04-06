"""
    Platform: LeetCode

    Link to Problem: https://leetcode.com/problems/valid-palindrome/

    Problem Statement: Given the root of a binary tree, return the postorder traversal of its nodes' values.

    Example 1:

    Input: root = [1,null,2,3]
    Output: [3,2,1]

    Example 2:

    Input: root = []
    Output: []

    Example 3:

    Input: root = [1]
    Output: [1]    

    Constraints:

    The number of the nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100    

    Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TreeTraversal:
    def __init__(self):
        self.res = []
    def postOrderTraversalRec(self, root: TreeNode) -> list[int]:
        if root != None:
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            self.res.append(root.val)
        
        return self.res

    def postOrderTraversalIte(self, root: TreeNode) -> list[int]:
        pass

treeTraversal = TreeTraversal()
# Post-Order Traversal Recursuve fashion
print(treeTraversal.postOrderTraversalRec())