# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        
        current = root
        pathArray = []
        
        def traverse(current, currentPath):
            if current is None:
                return pathArray
                
            
            currentPath += str(current.val)
            
            if current.left is not None:
                leftPath = currentPath
                leftPath += "->"
                traverse(current.left, leftPath)
            if current.right is not None:
                rightPath = currentPath
                rightPath += "->"
                traverse(current.right, rightPath)
                
            if current.left is None and current.right is None:   
                pathArray.append(currentPath)
                return pathArray
            
            
        traverse(current, "")
        return pathArray
