# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        
        currentP = p
        currentQ = q

        def traverse(currentP, currentQ):
            if currentP is None and currentQ is not None:
                return False

            if currentQ is None and currentP is not None:
                return False

            if currentP is None and currentQ is None:
                return True

            

            if currentP.val != currentQ.val:
                return False
            
                
            
            
            return traverse(currentP.left, currentQ.left) and traverse(currentP.right, currentQ.right)
            
        return traverse(currentP, currentQ)
