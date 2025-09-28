# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        

        current = root
        build = ''
        

        def traverse(current, build):
            if current is None:
                return
            left = 0
            right = 0

            build += str(current.val)

            if not current.left and not current.right:
                return int(build)

            if current.left:
                left = traverse(current.left, build)

            if current.right:
                right = traverse(current.right, build)

            return left + right
            
            


        return traverse(current, '')
