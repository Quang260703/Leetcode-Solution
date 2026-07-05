# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first_wrong = None
        self.second_wrong = None
        self.prev = TreeNode(float('-inf'))

        self.inorder(root)
        self.first_wrong.val, self.second_wrong.val = self.second_wrong.val, self.first_wrong.val


    def inorder(self, curr):
        if not curr:
            return

        self.inorder(curr.left)
        if curr.val < self.prev.val:
            if not self.first_wrong:
                self.first_wrong = self.prev
            self.second_wrong = curr
        self.prev = curr

        self.inorder(curr.right)
