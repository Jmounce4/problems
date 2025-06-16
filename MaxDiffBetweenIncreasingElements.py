class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        maxDiff = -1
        minNum = 0
        current = 0
        for j in range(1, len(nums)):
            current = nums[j] - nums[i]
            if nums[i] > nums[j] and j != len(nums):
                i = j
            if current > maxDiff:
                maxDiff = current
            
        if maxDiff == 0:
            return -1
        return maxDiff
