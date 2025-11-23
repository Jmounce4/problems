# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """


        def traverse(current):
            if current is None:
                return None

            if current.val == val:
                return current
            if val < current.val:
                return traverse(current.left)
            if val > current.val:
                return traverse(current.right)
        

        return traverse(root)
