# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        orderedList = []
        current = root

        def traverse(current):
            
            if current is None:
                return
            
            
            traverse(current.left)
            orderedList.append(current.val)
            traverse(current.right)
            
        traverse(current)
            
        return orderedList
