class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        current = root
        def traverse(current):
            if current is None:
                return 0
            
            leftDepth = traverse(current.left)
            rightDepth = traverse(current.right)
            return 1 + max(leftDepth, rightDepth)


           
            



       
        return traverse(current)
