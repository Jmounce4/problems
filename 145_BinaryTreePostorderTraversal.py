# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        

        current = root
        newArray = []
        def traverse(current):
            if current is None:
                return

            if current.left is None and current.right is None:
                newArray.append(current.val)
                return
                
            
            traverse(current.left)
            traverse(current.right)
            newArray.append(current.val)


        traverse(current)
        return newArray
