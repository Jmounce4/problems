class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        subsets = []
        current = []

        def traverse(current, index):

            if index == len(nums):
                subsets.append(current[:])
                return

            if index <= len(nums)-1:
            
                traverse(current + [nums[index]], index+1)
                traverse(current, index+1)


        traverse(current, 0)
        return subsets
