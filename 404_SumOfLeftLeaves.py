# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        current = root
        isLeft = False
        
        def traverse(current, isLeft):
            if current is None:
                return 0
                

            
            if isLeft and not current.left and not current.right:
                return current.val

            return traverse(current.left, True) + traverse(current.right, False)
            
            

        
        return traverse(current, isLeft)
        
