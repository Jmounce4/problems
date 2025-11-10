# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        self.max_diameter = 0

        
        current = root

        def traverse(current):
            if current is None:
                return 0

            leftDepth = traverse(current.left)
            rightDepth = traverse(current.right)
            
            self.max_diameter = max(self.max_diameter, leftDepth + rightDepth)
            
            return 1 + max(leftDepth, rightDepth)


        traverse(current)
        return self.max_diameter
