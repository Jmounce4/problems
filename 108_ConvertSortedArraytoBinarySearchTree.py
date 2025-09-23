# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        
        if not nums:
            return None

        def build(low, high):
            if low > high:
                return None
            mid = (low + high) // 2
            node = TreeNode(nums[mid])
            node.left = build(low, mid - 1)
            node.right = build(mid + 1, high)
            return node
        
        return build(0, len(nums)-1)
