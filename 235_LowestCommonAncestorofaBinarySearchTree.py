# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        

        current=root


        #if (p.val <= current.val and q.val >= current.val) or (p.val >= current.val and q.val <= current.val):
            #return current

        def traverse(current):
            if current is None:
                return
            
            #if (q.val <= current.val and p.val >= current.val) or (q.val >= current.val and p.val <= current.val):
                #return current
            if q.val < current.val and p.val < current.val:
                return traverse(current.left)
            elif q.val > current.val and p.val > current.val:
                return traverse(current.right)
            else:
                return current

        #if q.val < current.val:
            #return traverse(current.left)
        #else:
            #return traverse(current.right)
        
        return traverse(current)
        
