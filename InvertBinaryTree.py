# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        def traverse(current):
            
            if current is None:
                return
            temp = current.right
            current.right = current.left
            current.left = temp
            traverse(current.left)
            traverse(current.right)
            
        traverse(root)
        return root
