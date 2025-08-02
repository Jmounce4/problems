# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        current = root
        leftArray = []
        rightArray = []

        def traverseLeft(current):
            if current is not None:
                leftArray.append(current.val)

            if current.left is not None:
                traverseLeft(current.left)
            else:
                leftArray.append('null')
            
            if current.right is not None:
                traverseLeft(current.right)
            else:
                leftArray.append('null')
            
            return leftArray

        
        def traverseRight(current):
            if current is not None:
                rightArray.append(current.val)

            if current.right is not None:
                traverseRight(current.right)
            else:
                rightArray.append('null')
            
            if current.left is not None:
                traverseRight(current.left)
            else:
                rightArray.append('null')
            
            return rightArray


        if current is None:
            return True

        if current.left is not None and current.right is not None:
            if traverseLeft(current.left) == traverseRight(current.right):
                return True
            else:
                return False
        else:
            if current.left is not None or current.right is not None:
                return False
            else:
                return True
