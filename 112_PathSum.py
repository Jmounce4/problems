# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        
        current = root
        
        def traverse(current, sum):
            if current is not None:
                sum += current.val
            else:
                return
            

            if current.left is None and current.right is None:
                if sum == targetSum:
                    return True
            
            return(
                traverse(current.left, sum) or
                traverse(current.right, sum)
            )

            

        
        
        if traverse(current, 0):
            return True
        else:
            return False
